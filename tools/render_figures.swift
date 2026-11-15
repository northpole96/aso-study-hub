// Renders each <name>.html in a folder to <name>.png (the <svg> only, 3x, white background).
// Used by build_app_cards.py:  swift tools/render_figures.swift <in-dir> <out-dir>
import AppKit
import WebKit

let args = CommandLine.arguments
let inDir = URL(fileURLWithPath: args[1]), outDir = URL(fileURLWithPath: args[2])
let files = try FileManager.default.contentsOfDirectory(at: inDir, includingPropertiesForKeys: nil)
    .filter { $0.pathExtension == "html" }.sorted { $0.path < $1.path }

final class Renderer: NSObject, WKNavigationDelegate {
    let web = WKWebView(frame: NSRect(x: 0, y: 0, width: 640, height: 1200))
    var queue: [URL]
    init(_ q: [URL]) { queue = q; super.init(); web.navigationDelegate = self; web.appearance = NSAppearance(named: .aqua) }
    func next() {
        guard let f = queue.first else { NSApp.terminate(nil); return }
        web.loadFileURL(f, allowingReadAccessTo: URL(fileURLWithPath: "/"))
    }
    func webView(_ w: WKWebView, didFinish n: WKNavigation!) {
        // wait for fonts, then measure the svg
        w.evaluateJavaScript("document.fonts.ready.then(()=>0)") { _, _ in
            DispatchQueue.main.asyncAfter(deadline: .now() + 0.25) {
                w.evaluateJavaScript("(function(){var r=document.querySelector('svg').getBoundingClientRect();return [r.left,r.top,r.width,r.height]})()") { res, _ in
                    let f = self.queue.removeFirst()
                    guard let a = res as? [Double], a[2] > 0, a[3] > 0 else { print("skip", f.lastPathComponent); self.next(); return }
                    let pad = 8.0
                    let cfg = WKSnapshotConfiguration()
                    cfg.rect = CGRect(x: a[0] - pad, y: a[1] - pad, width: a[2] + 2 * pad, height: a[3] + 2 * pad)
                    cfg.snapshotWidth = NSNumber(value: 600)  // points; 1200 px on a retina Mac
                    w.takeSnapshot(with: cfg) { img, _ in
                        if let img, let tiff = img.tiffRepresentation, let rep = NSBitmapImageRep(data: tiff),
                           let png = rep.representation(using: .png, properties: [:]) {
                            let name = f.deletingPathExtension().lastPathComponent + ".png"
                            try? png.write(to: outDir.appendingPathComponent(name))
                        }
                        self.next()
                    }
                }
            }
        }
    }
}

let app = NSApplication.shared
app.setActivationPolicy(.prohibited)
let r = Renderer(files)
DispatchQueue.main.async { r.next() }
app.run()
