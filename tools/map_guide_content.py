# Map Guide · World + India. Chapters of places, each place pinned on one map.
# Place fields: n name · g [lon, lat] · x text (simple English) · y PYQ chips "2021 Q80" (optional, comma list)
#   r river name to light up (optional) · c country to light up · s Indian state to light up · k 1 = CHECK (not fully sure)
P = lambda n, g, x, **kw: dict(n=n, g=g, x=x, **kw)

CH = [
dict(id="passes", part="India", t="Himalayan passes and borders", intro=(
 "The Himalaya is a wall, and the passes are its doors. Read them from west to east, the way the border runs. "
 "In Ladakh and Kashmir the doors lead to Pakistan-held land and to Tibet. In Himachal and Uttarakhand they are old "
 "trade and pilgrim routes to Tibet. In Sikkim and Arunachal they face China. The exam likes to pair a pass with the wrong "
 "state, so learn each one with its state, and with the road or tunnel that now goes under or over it."), P=[
 P("Karakoram Pass", [77.83, 35.51], "The highest pass on the old Silk Road, between Ladakh and Xinjiang (China). It lies just east of the Siachen area."),
 P("Siachen Glacier", [77.15, 35.42], "In the Karakoram, Ladakh. It is the highest battlefield in the world. India took it in Operation Meghdoot in 1984.", s="Ladakh"),
 P("Khardung La", [77.60, 34.28], "North of Leh, Ladakh. The road over it leads to the Nubra valley and on to Siachen."),
 P("Zoji La", [75.47, 34.28], "Joins Srinagar (Kashmir) to Kargil and Leh (Ladakh). The Zojila tunnel is being built under it, so the road stays open in winter. The Z-Morh (Sonamarg) tunnel on the same road opened in January 2025."),
 P("Banihal Pass", [75.20, 33.48], "In the Pir Panjal range, it joins Jammu to the Kashmir valley. The Jawahar tunnel and the newer Banihal–Qazigund tunnel pass under it."),
 P("Rohtang Pass", [77.25, 32.37], "Joins the Kullu valley (Manali) to Lahaul in Himachal Pradesh. The Atal Tunnel (2020, about 9 km) runs under it."),
 P("Bara Lacha La", [77.42, 32.76], "In Lahaul, Himachal Pradesh, on the Manali–Leh road. The Chandra and Bhaga rivers start near it and join to form the Chenab.", y="2021 Q80", s="Himachal Pradesh"),
 P("Shipki La", [78.75, 31.83], "In Kinnaur, Himachal Pradesh. The Sutlej enters India from Tibet through this gap. It is a trade post with China."),
 P("Mana Pass", [79.42, 31.07], "In Chamoli, Uttarakhand, north of Badrinath. Mana is called the last village of India.", y="2021 Q80", s="Uttarakhand"),
 P("Niti Pass", [79.89, 30.97], "Also in Chamoli, Uttarakhand, east of Mana. An old trade route to Tibet."),
 P("Lipulekh Pass", [80.98, 30.23], "In Pithoragarh, Uttarakhand, near the India–Nepal–China meeting point. Pilgrims take it to Kailash–Mansarovar."),
 P("Nathu La", [88.83, 27.39], "In Sikkim, on the border with Tibet. It was reopened for trade in 2006. Pilgrims also use it for Kailash.", s="Sikkim"),
 P("Jelep La", [88.95, 27.33], "Also in Sikkim, just south-east of Nathu La, on the old Kalimpong–Lhasa route. The 2021 paper paired it with Arunachal Pradesh as the wrong pair.", y="2021 Q80"),
 P("Doklam", [89.00, 27.28], "A plateau where Bhutan, China and India (Sikkim) meet. Indian and Chinese troops faced each other here for 73 days in 2017."),
 P("Bum La", [91.95, 27.70], "North of Tawang, Arunachal Pradesh, on the border with Tibet. A border meeting point for Indian and Chinese officers.", k=1),
 P("Sela Pass and Tunnel", [92.10, 27.50], "In West Kameng, Arunachal Pradesh, on the only road to Tawang. The Border Roads Organisation built the Sela Tunnel below the pass; it opened in March 2024.", y="2021 Q89", s="Arunachal Pradesh"),
 P("Diphu Pass", [97.35, 28.17], "At the far east end of Arunachal Pradesh, where India, China and Myanmar meet."),
 P("Galwan Valley", [78.20, 34.75], "In eastern Ladakh, on the Line of Actual Control. Indian and Chinese soldiers clashed here in June 2020."),
 P("Pangong Tso", [78.70, 33.75], "A long, salty lake in eastern Ladakh. About two-thirds of it lies in Tibet. The Line of Actual Control crosses it."),
]),
dict(id="rivers", part="India", t="Rivers: where they rise, where they end", intro=(
 "A river question in this exam is almost always about where a river rises, which way it flows, or what stands on it. "
 "The Himalayan rivers (Indus, Ganga, Brahmaputra) are fed by snow, so they flow all year. The peninsular rivers are fed by rain. "
 "Most of them flow east into the Bay of Bengal and build deltas: Mahanadi, Godavari, Krishna, Kaveri. "
 "Two flow west into the Arabian Sea in rift valleys and end in estuaries, with no delta: the Narmada and the Tapi. "
 "Remember that pair, because it is the most-asked river fact."), P=[
 P("Indus (source)", [81.30, 31.20], "The Indus rises in Tibet near Lake Mansarovar, enters Ladakh, then turns into Pakistan. Its five eastern tributaries (Jhelum, Chenab, Ravi, Beas, Sutlej) give Punjab its name.", r="Indus"),
 P("Gangotri (Gaumukh)", [79.08, 30.92], "The Bhagirathi, the head-stream of the Ganga, comes out of the Gangotri glacier at Gaumukh in Uttarakhand.", r="Ganges"),
 P("Devprayag", [78.60, 30.15], "Here the Bhagirathi and the Alaknanda meet. From this point the river is called the Ganga."),
 P("Yamunotri", [78.45, 31.01], "The Yamuna rises at the Yamunotri glacier in Uttarakhand. It joins the Ganga at Prayagraj.", r="Yamuna"),
 P("Prayagraj (Sangam)", [81.88, 25.42], "The Ganga and Yamuna meet here, with the hidden Saraswati of legend. The Kumbh Mela is held at this Sangam."),
 P("Brahmaputra in India", [95.30, 28.10], "The Brahmaputra starts in Tibet as the Yarlung Tsangpo, makes a great U-turn around Namcha Barwa, and enters Arunachal as the Siang (Dihang). In Assam it is the Brahmaputra, and in Bangladesh the Jamuna.", r="Brahmaputra"),
 P("Amarkantak", [81.75, 22.68], "On the Maikal range, Madhya Pradesh. The Narmada (west) and the Son (north-east) both rise here.", y="2021 Q72"),
 P("Narmada mouth (Bharuch)", [72.98, 21.70], "The Narmada flows west in a rift valley between the Vindhya and Satpura and ends in the Gulf of Khambhat in an estuary.", r="Narmada", y="2021 Q72"),
 P("Sardar Sarovar Dam", [73.75, 21.83], "On the Narmada in Gujarat. The Statue of Unity (Sardar Patel, 182 m) stands just below it.", r="Narmada"),
 P("Multai (Tapi source)", [78.25, 21.77], "The Tapi rises at Multai in Betul, Madhya Pradesh, in the Satpura range. It flows west past Surat into the Gulf of Khambhat.", r="Tapi", y="2021 Q72"),
 P("Sihawa (Mahanadi source)", [81.93, 20.30], "The Mahanadi rises near Sihawa in Dhamtari, Chhattisgarh, and flows east through Odisha.", r="Mahanadi"),
 P("Hirakud Dam", [83.87, 21.53], "On the Mahanadi near Sambalpur, Odisha. One of the longest earthen dams in the world (1957).", r="Mahanadi"),
 P("Trimbakeshwar (Godavari source)", [73.53, 19.93], "The Godavari rises near Nashik, Maharashtra. It is the longest peninsular river, called the Dakshin Ganga.", r="Godavari"),
 P("Mahabaleshwar (Krishna source)", [73.66, 17.92], "The Krishna rises at Mahabaleshwar in the Western Ghats, Maharashtra, and flows east to the Bay of Bengal in Andhra Pradesh.", r="Krishna"),
 P("Nagarjuna Sagar Dam", [79.31, 16.57], "A large masonry dam on the Krishna, on the Telangana–Andhra Pradesh border.", r="Krishna"),
 P("Talakaveri (Kaveri source)", [75.49, 12.39], "The Kaveri rises on the Brahmagiri hills in Kodagu (Coorg), Karnataka. Its water is shared by Karnataka and Tamil Nadu after a long dispute.", r="Kaveri"),
 P("Bhakra Dam", [76.43, 31.41], "On the Sutlej in Himachal Pradesh. Its lake is the Gobind Sagar. Nehru called such dams the temples of modern India."),
 P("Tehri Dam", [78.48, 30.38], "On the Bhagirathi in Uttarakhand. It is the tallest dam in India."),
]),
dict(id="relief", part="India", t="Mountains, plateaus and deserts", intro=(
 "India's land has three big parts: the young Himalaya in the north, the flat plains of the Ganga in the middle, and the old, hard Peninsular plateau in the south. "
 "The plateau is ringed by ranges: the Aravalli (the oldest fold mountains in India) in the north-west, the Vindhya and Satpura across the middle, and the Western and Eastern Ghats along the coasts. "
 "For each range, learn its highest point. For each plateau, learn what it is rich in."), P=[
 P("K2 (Godwin-Austen)", [76.51, 35.88], "In the Karakoram, in Gilgit-Baltistan (Indian territory held by Pakistan). It is the second highest peak in the world and the highest peak of India by India's map."),
 P("Kanchenjunga", [88.15, 27.70], "On the Sikkim–Nepal border. The third highest peak in the world and the highest peak within India's present borders.", s="Sikkim"),
 P("Nanda Devi", [79.97, 30.38], "In Uttarakhand. The highest peak that lies wholly inside India. The Nanda Devi and Valley of Flowers parks are a World Heritage Site."),
 P("Guru Shikhar", [72.78, 24.65], "On Mount Abu, Rajasthan. The highest point of the Aravalli, India's oldest fold mountains."),
 P("Vindhya Range", [78.00, 23.70], "Runs across central India north of the Narmada. It is the old line between north and south India."),
 P("Satpura Range", [77.50, 21.90], "Runs south of the Narmada and north of the Tapi. Dhupgarh (Pachmarhi) is its highest point."),
 P("Western Ghats (Sahyadri)", [73.80, 17.50], "A steep wall along the west coast from Gujarat to Kerala. It stops the monsoon winds, so the coast is wet and the land behind is dry. A World Heritage Site and a biodiversity hotspot."),
 P("Anamudi", [77.06, 10.17], "In Kerala, in the Anaimalai hills. The highest peak of the Western Ghats and of south India (2,695 m)."),
 P("Doddabetta", [76.73, 11.40], "The highest peak of the Nilgiri hills, near Ooty, Tamil Nadu. The Nilgiris are where the Western and Eastern Ghats meet."),
 P("Eastern Ghats", [82.50, 18.00], "A broken chain of hills along the east coast, cut through by the Mahanadi, Godavari, Krishna and Kaveri. They are lower and older than the Western Ghats."),
 P("Deccan Plateau", [77.50, 17.20], "The big lava plateau of Maharashtra and the south. Its basalt makes black (regur) soil, good for cotton."),
 P("Chota Nagpur Plateau", [85.00, 23.50], "Jharkhand and nearby. The mineral heartland of India: coal, iron ore, mica, bauxite. Ranchi is on it."),
 P("Shillong (Meghalaya) Plateau", [91.50, 25.50], "Made of the Garo, Khasi and Jaintia hills. It is a broken-off piece of the Peninsular plateau."),
 P("Mawsynram", [91.58, 25.30], "In the Khasi hills, Meghalaya. One of the wettest places on earth; nearby Cherrapunji (Sohra) held the record before.", s="Meghalaya"),
 P("Thar Desert", [71.00, 27.00], "The Great Indian Desert in Rajasthan and Gujarat. It stays dry because the Aravalli run parallel to the monsoon winds: they do not block the winds, so the winds pass over without dropping rain."),
]),
dict(id="coasts", part="India", t="Coasts, islands and lakes", intro=(
 "India's coast is about 7,500 km long. The west coast is narrow, with lagoons in Kerala. The east coast is wide, with deltas and big lagoons like Chilika and Pulicat. "
 "Off the coasts lie two island groups: Lakshadweep (coral) in the Arabian Sea and the Andaman and Nicobar Islands (hills of a drowned mountain chain) in the Bay of Bengal. "
 "Lake questions usually ask for a superlative: the largest, the longest, the saltiest. Pin each superlative to its lake."), P=[
 P("Rann of Kutch", [70.00, 23.90], "A huge salt marsh in Gujarat. It floods in the monsoon and dries to white salt in winter. The wild ass sanctuary is here."),
 P("Gulf of Khambhat", [72.40, 21.60], "Also called the Gulf of Cambay, in Gujarat. The Narmada, Tapi, Mahi and Sabarmati end here. Its tides are very high."),
 P("Gulf of Kutch", [69.60, 22.60], "North of the Kathiawar peninsula. India's first Marine National Park is here (1980)."),
 P("Palk Strait", [79.50, 10.00], "The sea between Tamil Nadu and Sri Lanka, north of Adam's Bridge."),
 P("Adam's Bridge (Ram Setu)", [79.50, 9.12], "A chain of shoals from Rameswaram (Pamban Island) to Mannar Island in Sri Lanka. It separates the Palk Strait from the Gulf of Mannar."),
 P("Gulf of Mannar", [79.10, 8.90], "South of Rameswaram. A marine National Park and Biosphere Reserve with coral reefs and the dugong (sea cow)."),
 P("Kanyakumari", [77.54, 8.08], "The southern tip of mainland India, where the Arabian Sea, Indian Ocean and Bay of Bengal meet."),
 P("Vembanad Lake", [76.38, 9.60], "In Kerala. The longest lake in India. The Nehru Trophy boat race is held on its Punnamada stretch."),
 P("Pulicat Lake", [80.30, 13.55], "On the Andhra Pradesh–Tamil Nadu border. The second largest lagoon in India. Sriharikota island lies between it and the sea."),
 P("Chilika Lake", [85.33, 19.70], "In Odisha. The largest brackish-water lagoon in India and India's first Ramsar site (1981, with Keoladeo). Irrawaddy dolphins live here.", s="Odisha"),
 P("Sambhar Lake", [75.08, 26.92], "In Rajasthan. The largest inland salt lake in India."),
 P("Wular Lake", [74.57, 34.36], "In Kashmir. The largest freshwater lake in India. The Jhelum flows through it."),
 P("Loktak Lake", [93.79, 24.53], "In Manipur. Famous for phumdis, floating mats of plants. Keibul Lamjao on it is the only floating national park in the world, home of the sangai deer.", s="Manipur"),
 P("Majuli", [94.20, 26.95], "A large river island in the Brahmaputra, Assam. In 2016 it became India's first island district."),
 P("Kavaratti (Lakshadweep)", [72.64, 10.56], "The capital of Lakshadweep, India's coral islands in the Arabian Sea. The Nine Degree Channel separates them from Minicoy."),
 P("Ten Degree Channel", [92.50, 10.00], "The sea that separates the Andaman Islands (north) from the Nicobar Islands (south)."),
 P("Barren Island", [93.86, 12.28], "In the Andaman Sea. The only active volcano in India (and in South Asia)."),
 P("Indira Point", [93.84, 6.75], "On Great Nicobar Island. The southernmost point of India."),
]),
dict(id="parks", part="India", t="National parks and wildlife", intro=(
 "A park question asks one of three things: which animal it protects, which state it is in, or what is special about it (first, largest, floating, World Heritage). "
 "Group them by animal: the one-horned rhino in Assam, the Asiatic lion only in Gir, the tiger across many reserves, the snow leopard in Ladakh, and the cheetah, brought back from Africa, at Kuno."), P=[
 P("Jim Corbett National Park", [78.77, 29.53], "In Uttarakhand. India's first national park (1936, as Hailey National Park). Project Tiger was launched here in 1973."),
 P("Kaziranga", [93.37, 26.58], "In Assam, on the Brahmaputra. Home of most of the world's one-horned rhinos. A World Heritage Site.", s="Assam"),
 P("Gir", [70.80, 21.12], "In Gujarat. The only natural home of the Asiatic lion.", s="Gujarat"),
 P("Kuno National Park", [77.33, 25.55], "In Sheopur, Madhya Pradesh. Cheetahs from Namibia were released here in September 2022, seventy years after the cheetah died out in India."),
 P("Sundarbans", [88.85, 21.95], "In West Bengal (and Bangladesh). The largest mangrove forest in the world, on the Ganga–Brahmaputra delta. Home of the Royal Bengal tiger."),
 P("Keoladeo (Bharatpur)", [77.52, 27.17], "In Rajasthan. A wetland famous for winter birds such as the Siberian crane. A World Heritage Site and Ramsar site."),
 P("Hemis National Park", [77.40, 33.90], "In Ladakh. The largest national park in India, known for the snow leopard."),
 P("Great Himalayan National Park", [77.50, 31.75], "In Kullu, Himachal Pradesh. A World Heritage Site since 2014."),
 P("Valley of Flowers", [79.60, 30.73], "In Chamoli, Uttarakhand. Alpine meadows full of flowers in the monsoon. World Heritage, together with Nanda Devi."),
 P("Silent Valley", [76.43, 11.08], "In Palakkad, Kerala. A people's movement stopped a dam on the Kunthipuzha river, and it became a national park in 1984. Home of the lion-tailed macaque."),
 P("Periyar", [77.17, 9.47], "In the hills of Kerala. A tiger reserve around a lake made by the Mullaperiyar dam. Known for elephants."),
 P("Dehing Patkai", [95.45, 27.30], "In eastern Assam, called the Jeypore rainforest. The 'Save Dehing Patkai' online campaign helped make it a national park in 2021.", y="2021 Q92"),
 P("Bhadla Solar Park", [71.92, 27.54], "In Jodhpur district, Rajasthan, in the Thar. About 2,245 MW; often called the world's largest solar park in 2022 lists.", y="2021 Q98"),
]),
dict(id="defence", part="India", t="Defence, space and training", intro=(
 "Defence questions often ask where something is based: a command, an academy, a test range, a launch pad. "
 "The three naval commands sit on the three seas: Mumbai (west), Visakhapatnam (east) and Kochi (south, for training). "
 "Missiles are tested off the Odisha coast; satellites are launched from Sriharikota because a rocket fired east over the sea gets a push from the earth's spin and falls into empty water if it fails."), P=[
 P("Port Blair (Sri Vijaya Puram)", [92.73, 11.62], "Capital of the Andaman and Nicobar Islands, renamed in 2024. Base of the Andaman and Nicobar Command (2001), India's only tri-service command. INS Utkrosh, a naval air station, is here.", y="2021 Q85"),
 P("Sriharikota", [80.23, 13.72], "An island in Andhra Pradesh, next to Pulicat Lake. ISRO's Satish Dhawan Space Centre launches rockets from here."),
 P("Thumba", [76.87, 8.53], "Near Thiruvananthapuram, Kerala. India's first rocket was launched from here in 1963, because it lies close to the magnetic equator."),
 P("Abdul Kalam Island", [87.08, 20.76], "Off the Odisha coast, formerly Wheeler Island. India's main missile test site (Agni and others). Chandipur, near Balasore, is the other test range."),
 P("Pokhran", [71.92, 26.92], "In Jaisalmer, Rajasthan. India's nuclear tests: Smiling Buddha (1974) and Operation Shakti (1998)."),
 P("Mumbai", [72.83, 18.93], "Headquarters of the Western Naval Command."),
 P("Visakhapatnam", [83.28, 17.69], "Headquarters of the Eastern Naval Command, and the base of India's nuclear submarines."),
 P("Kochi", [76.27, 9.96], "Headquarters of the Southern Naval Command (the training command). INS Vikrant, the first home-built aircraft carrier, was built at Cochin Shipyard."),
 P("Karwar (INS Kadamba)", [74.12, 14.80], "In Karnataka. A large naval base built under Project Seabird."),
 P("Khadakwasla (NDA)", [73.77, 18.44], "Near Pune. The National Defence Academy trains cadets of all three services together."),
 P("Dehradun (IMA)", [78.00, 30.33], "The Indian Military Academy trains army officers. The Rashtriya Indian Military College is also here."),
 P("Ezhimala", [75.20, 12.03], "In Kannur, Kerala. The Indian Naval Academy, the largest in Asia."),
 P("Gurugram (ISA and INDU)", [76.95, 28.40], "The International Solar Alliance has its headquarters at Gurugram, Haryana. The Indian National Defence University is coming up at Binola, nearby.", y="2021 Q52, 2021 Q81", s="Haryana"),
 P("Bengaluru (HAL)", [77.66, 12.96], "Hindustan Aeronautics Limited builds the Tejas fighter and the ALH Dhruv helicopter here. ISRO's headquarters is also in Bengaluru."),
]),
dict(id="straits", part="World", t="Straits, canals and capes", intro=(
 "A strait is a narrow sea between two pieces of land; a canal is a strait people dug. Both are choke points: block one, and ships must go a long way round. "
 "That is why they keep coming into the news. Learn each with the two lands on its sides and the two waters it joins."), P=[
 P("Strait of Hormuz", [56.40, 26.50], "Between Iran and Oman. Joins the Persian Gulf to the Gulf of Oman. About a fifth of the world's oil passes through it."),
 P("Bab-el-Mandeb", [43.40, 12.60], "Between Yemen and Djibouti. Joins the Red Sea to the Gulf of Aden. Attacks on ships here from late 2023 pushed many ships round Africa."),
 P("Suez Canal", [32.35, 30.60], "In Egypt. Joins the Mediterranean to the Red Sea (opened 1869). The shortest sea route from Europe to India."),
 P("Strait of Malacca", [100.50, 3.00], "Between Malaysia and Sumatra (Indonesia). Joins the Andaman Sea to the South China Sea. One of the busiest sea lanes in the world."),
 P("Strait of Gibraltar", [-5.60, 35.97], "Between Spain and Morocco. Joins the Mediterranean to the Atlantic."),
 P("Bosporus", [29.05, 41.12], "In Turkey, through Istanbul. Joins the Black Sea to the Sea of Marmara. It divides Europe from Asia."),
 P("Kerch Strait", [36.50, 45.30], "Joins the Black Sea to the Sea of Azov, between Crimea and Russia.", y="2021 Q17"),
 P("Strait of Dover", [1.45, 51.00], "Between England and France; the narrowest part of the English Channel. The Channel Tunnel runs under it."),
 P("Panama Canal", [-79.68, 9.08], "In Panama. Joins the Atlantic (Caribbean) to the Pacific (opened 1914). Ships are lifted by locks."),
 P("Bering Strait", [-169.00, 65.80], "Between Russia (Asia) and Alaska (USA). Joins the Pacific to the Arctic Ocean. The International Date Line runs through it."),
 P("Taiwan Strait", [119.50, 24.50], "Between mainland China and Taiwan. Joins the East and South China Seas."),
 P("Mozambique Channel", [41.00, -18.00], "Between Mozambique and Madagascar, in the Indian Ocean."),
 P("Cape of Good Hope", [18.47, -34.36], "Near Cape Town, South Africa. Ships go round it when the Suez route is closed. Vasco da Gama sailed round it to reach Calicut in 1498."),
]),
dict(id="worldrelief", part="World", t="Mountains, volcanoes and trenches", intro=(
 "Mountains come in kinds, and the exam asks you to match the kind with an example. Fold mountains form where plates push together: young ones are high and sharp (Himalaya, Alps, Andes, Rockies), old ones are low and worn (Appalachians, Urals, Aravalli). "
 "Block mountains rise between faults, next to a sunken rift valley. Volcanoes cluster along plate edges, mostly round the Pacific Ring of Fire, or sit over hot spots like Hawaii."), P=[
 P("Mount Everest", [86.93, 27.99], "On the Nepal–Tibet border. The highest peak on earth (8,849 m)."),
 P("Alps", [10.00, 46.40], "Young fold mountains of Europe. Mont Blanc is the highest peak."),
 P("Andes", [-70.00, -20.00], "Young fold mountains along the west of South America; the longest mountain range on land. The Nazca plate dives under the South American plate here.", y="2021 Q61"),
 P("Rockies", [-110.00, 45.00], "Young fold mountains of western North America."),
 P("Appalachians", [-80.00, 38.00], "Old fold mountains in the eastern USA, worn low over time.", y="2021 Q64"),
 P("Ural Mountains", [59.50, 58.00], "Old fold mountains in Russia. They mark the line between Europe and Asia."),
 P("Black Forest", [8.20, 48.20], "A block mountain in south-west Germany, beside the Rhine rift valley. The Vosges in France are its twin.", y="2021 Q64"),
 P("Scottish Highlands", [-4.50, 57.00], "Relict (left-over) mountains, the worn stumps of a very old range.", y="2021 Q64"),
 P("Aleutian Islands", [-176.00, 52.00], "A volcanic island arc west of Alaska, on the Ring of Fire. Many active volcanoes.", y="2021 Q65"),
 P("Iceland", [-19.00, 64.90], "Sits on the Mid-Atlantic Ridge, where the North American and Eurasian plates move apart. Full of volcanoes and geysers.", y="2021 Q61"),
 P("Hawaii", [-155.50, 19.60], "Volcanic islands in the middle of the Pacific plate, made by a hot spot. Mauna Loa and Kilauea are active."),
 P("Mount Fuji", [138.73, 35.36], "Japan's highest mountain, a dormant volcano on the Ring of Fire."),
 P("Kilimanjaro", [37.35, -3.07], "In Tanzania. The highest mountain in Africa, a dormant volcano near the equator with snow on top."),
 P("Great Rift Valley", [36.00, -1.00], "In East Africa, where the African plate is slowly splitting. Its lakes include Tanganyika and Malawi."),
 P("Mariana Trench", [142.20, 11.35], "In the western Pacific near Guam. The deepest point of the oceans, the Challenger Deep (about 11 km)."),
 P("Dead Sea", [35.50, 31.50], "Between Jordan and Israel/West Bank. The lowest land on earth (about 430 m below sea level) and very salty."),
]),
dict(id="lands", part="World", t="Grasslands and deserts", intro=(
 "The temperate grasslands have a different name on each continent, and the 2021 paper set a trap with them. Learn the set together: Prairies in North America, Pampas in South America, Veldt in South Africa, Steppes in Eurasia, Downs in Australia. "
 "Tropical grasslands are savannas: Llanos and Campos in South America, the Serengeti in Africa. Deserts form under dry, sinking air or behind mountains, and cold currents make coastal deserts like the Atacama and Namib."), P=[
 P("Prairies", [-100.00, 45.00], "Temperate grassland of North America (USA and Canada). Now the wheat belt.", y="2021 Q63"),
 P("Pampas", [-62.00, -35.00], "Temperate grassland of Argentina and Uruguay, South America. The 2021 trap put it in North America.", y="2021 Q63"),
 P("Veldt", [27.00, -27.00], "Temperate grassland of South Africa.", y="2021 Q63", c="South Africa"),
 P("Steppes", [60.00, 48.00], "Temperate grassland of Eurasia, from Ukraine through Kazakhstan.", y="2021 Q63"),
 P("Downs", [145.00, -27.00], "Temperate grassland of Australia, known for sheep."),
 P("Llanos", [-68.00, 7.00], "Tropical grassland of Venezuela and Colombia, along the Orinoco."),
 P("Campos", [-48.00, -15.00], "Tropical grassland of the Brazilian highlands."),
 P("Serengeti", [34.80, -2.30], "Savanna in Tanzania, famous for the great migration of wildebeest."),
 P("Sahara", [10.00, 23.00], "The largest hot desert in the world, across North Africa."),
 P("Kalahari", [22.00, -23.00], "A semi-desert in Botswana and nearby. The San (Bushmen) live here."),
 P("Atacama", [-69.50, -24.00], "In northern Chile. The driest hot desert on earth, made by the cold Humboldt current offshore."),
 P("Gobi", [105.00, 43.00], "A cold desert in Mongolia and China, in the rain shadow of the Himalaya."),
 P("Rub' al Khali", [50.00, 20.00], "The Empty Quarter of Arabia, the largest sand desert in the world."),
]),
dict(id="worldrivers", part="World", t="World rivers, deltas and lakes", intro=(
 "A delta forms where a river drops its silt faster than the sea can wash it away. Its shape tells you how calm the sea is: the Nile's fan is arcuate, the Mississippi's long fingers make a bird-foot. "
 "Where tides are strong, the river ends in an open estuary instead, like the Amazon or the Narmada. For lakes, again learn the superlatives."), P=[
 P("Mississippi delta", [-89.30, 29.10], "Ends in the Gulf of Mexico in a bird-foot delta: long fingers of silt.", y="2021 Q66", r="Mississippi"),
 P("Nile delta", [31.00, 31.00], "A fan-shaped (arcuate) delta in Egypt. The Nile is the longest river in the world.", r="Nile"),
 P("Lake Victoria", [33.00, -1.00], "In Uganda, Kenya and Tanzania. The largest lake in Africa and the source of the White Nile."),
 P("Amazon mouth", [-50.00, 0.00], "The Amazon carries more water than any other river. It meets the Atlantic near the equator in a wide estuary.", r="Amazonas"),
 P("Niger delta", [6.00, 4.80], "In Nigeria, on the Gulf of Guinea. Rich in oil."),
 P("Congo river", [12.40, -6.00], "Crosses the equator twice. Second in the world by volume of water."),
 P("Danube", [29.50, 45.10], "Flows from Germany to the Black Sea through more countries than any other river (ten).", r="Danube"),
 P("Caspian Sea", [50.50, 41.50], "The largest lake in the world, salty, between Europe and Asia."),
 P("Lake Baikal", [108.00, 53.50], "In Siberia, Russia. The deepest and oldest lake, holding about a fifth of the world's unfrozen fresh water."),
 P("Lake Superior", [-87.50, 47.70], "On the USA–Canada border. The largest freshwater lake by area."),
 P("Lake Titicaca", [-69.30, -15.80], "On the Peru–Bolivia border. The highest navigable lake."),
 P("Yangtze mouth", [121.80, 31.40], "The Yangtze (Chang Jiang) is the longest river in Asia. The Three Gorges Dam is on it. Shanghai stands at its mouth.", r="Yangtze"),
]),
dict(id="winds", part="World", t="Local winds and ocean currents", intro=(
 "Local winds have names, and the exam matches name to place. Cold winds slide down from high land (Bora, Mistral); hot dry winds blow out of deserts (Khamsin, Sirocco, Harmattan, Loo); warm dry winds come down the far side of mountains (Chinook, Foehn). "
 "Ocean currents follow one simple rule: warm currents flow from the equator toward the poles, and cold currents flow from the poles toward the equator. Cold currents keep the air dry, so they make coastal deserts, and they bring up food for fish, so they make rich fishing grounds."), P=[
 P("Bora", [14.50, 45.30], "A cold, dry wind rushing down to the Adriatic coast (Croatia, Trieste).", y="2021 Q67"),
 P("Mistral", [4.80, 44.00], "A cold north wind down the Rhône valley in southern France.", y="2021 Q67"),
 P("Khamsin", [31.20, 28.00], "A hot, dusty wind in Egypt and Arabia in spring.", y="2021 Q67"),
 P("Sirocco", [13.00, 37.80], "A hot wind from the Sahara that reaches Sicily and southern Italy."),
 P("Harmattan", [-1.00, 12.00], "A dry wind from the Sahara over West Africa. It is called the doctor because it brings relief from damp heat."),
 P("Chinook", [-113.00, 50.50], "A warm, dry wind down the east side of the Rockies. Called the snow eater."),
 P("Foehn", [10.00, 47.20], "A warm, dry wind down the north side of the Alps. It ripens grapes and melts snow."),
 P("Santa Ana", [-117.50, 34.00], "A hot, dry wind in southern California that spreads wildfires."),
 P("Loo", [80.00, 26.50], "A hot, dry wind over north India in May and June."),
 P("Kalbaisakhi (Nor'wester)", [88.40, 22.60], "Evening thunderstorms in West Bengal and Assam in April–May, good for tea, jute and rice."),
 P("Mango showers", [76.30, 10.50], "Pre-monsoon showers in Kerala and Karnataka that help mangoes ripen. In Karnataka, coffee blossom showers."),
 P("Gulf Stream", [-75.00, 35.00], "A warm current up the east coast of the USA and across to Europe. It keeps north-west Europe mild in winter."),
 P("Labrador Current", [-55.00, 50.00], "A cold current down past Canada. It meets the Gulf Stream at the Grand Banks, a rich fishing ground."),
 P("Kuroshio", [135.00, 32.00], "A warm current past Japan, the Pacific twin of the Gulf Stream."),
 P("Oyashio", [147.00, 42.00], "A cold current from the north that meets the Kuroshio near Japan.", y="2021 Q62"),
 P("Canaries Current", [-17.00, 27.00], "A cold current off north-west Africa.", y="2021 Q62"),
 P("Humboldt (Peru) Current", [-78.00, -15.00], "A cold current up the coast of Peru and Chile. It makes the Atacama dry and the fishing rich. El Niño weakens it."),
 P("Benguela Current", [12.00, -25.00], "A cold current up the coast of south-west Africa. It makes the Namib desert."),
 P("Agulhas Current", [31.00, -32.00], "A warm current down the east coast of South Africa."),
 P("West Wind Drift", [0.00, -50.00], "A cold current that circles Antarctica, the only current that goes all the way round the earth. It is in the southern hemisphere.", y="2021 Q62"),
 P("Somali Current", [52.00, 7.00], "Off the Horn of Africa. The only big current that reverses its direction with the monsoon."),
]),
dict(id="hq", part="World", t="Headquarters of world bodies", intro=(
 "Headquarters questions are easy marks if the cities are clear in your head. Most bodies sit in a few cities: Geneva (health, trade, labour, weather, Red Cross), New York (the UN itself), Washington (IMF, World Bank), Paris (UNESCO, OECD), Vienna (IAEA, OPEC) and Brussels (NATO, EU). "
 "The Asian banks sit in Asia: ADB in Manila, AIIB in Beijing, NDB in Shanghai. Regional groups sit with a member: SAARC in Kathmandu, ASEAN in Jakarta, BIMSTEC in Dhaka."), P=[
 P("New York", [-73.97, 40.75], "Headquarters of the United Nations."),
 P("Geneva", [6.13, 46.23], "WHO, WTO, ILO, WMO, the UN Human Rights Council and the Red Cross (ICRC)."),
 P("Washington, DC", [-77.04, 38.90], "The IMF and the World Bank."),
 P("Paris", [2.30, 48.85], "UNESCO, OECD and the International Energy Agency."),
 P("Vienna", [16.37, 48.21], "The IAEA (nuclear watchdog) and OPEC."),
 P("Brussels", [4.35, 50.85], "NATO and the main seat of the European Union. NATO had 30 members in 2022 and 32 after Finland and Sweden joined.", y="2021 Q54, 2021 Q55"),
 P("The Hague", [4.30, 52.08], "The International Court of Justice and the International Criminal Court."),
 P("Rome", [12.49, 41.88], "The Food and Agriculture Organization (FAO) and the World Food Programme."),
 P("Lyon", [4.85, 45.77], "Interpol."),
 P("London", [-0.13, 51.50], "The Commonwealth Secretariat and the International Maritime Organization."),
 P("Nairobi", [36.82, -1.23], "UN Environment Programme (UNEP) and UN-Habitat."),
 P("Addis Ababa", [38.75, 9.03], "The African Union."),
 P("Manila", [121.06, 14.59], "The Asian Development Bank."),
 P("Beijing", [116.40, 39.90], "The Asian Infrastructure Investment Bank (AIIB) and the SCO Secretariat."),
 P("Shanghai", [121.47, 31.23], "The New Development Bank, the BRICS bank."),
 P("Kathmandu", [85.32, 27.70], "The SAARC Secretariat."),
 P("Jakarta", [106.85, -6.20], "The ASEAN Secretariat."),
 P("Dhaka", [90.41, 23.81], "The BIMSTEC Secretariat."),
]),
dict(id="news", part="World", t="Places in the news, 2025–26", intro=(
 "The 2025 paper asked many questions on events: who hosted a summit, where an exercise was held, where an attack or an operation happened. "
 "This chapter pins the places behind the biggest stories of 2025 and 2026. Facts marked CHECK came from news reports and should be looked up again before the exam."), P=[
 P("Pahalgam", [75.32, 34.01], "In Anantnag, Kashmir. Terrorists killed 26 people, mostly tourists, at Baisaran meadow on 22 April 2025."),
 P("Operation Sindoor targets", [71.68, 29.40], "On 7 May 2025 India struck nine terror sites in Pakistan and Pakistan-occupied Kashmir, including Bahawalpur (Jaish-e-Mohammed) and Muridke (Lashkar-e-Taiba)."),
 P("Chenab Bridge", [74.88, 33.15], "In Reasi, Jammu and Kashmir. The world's highest railway arch bridge, opened in June 2025 on the line to the Kashmir valley."),
 P("New Pamban Bridge", [79.20, 9.28], "Joins Rameswaram island to the mainland, Tamil Nadu. India's first vertical-lift sea bridge, opened in April 2025."),
 P("Auli and Mahajan (Yudh Abhyas 2026)", [79.56, 30.53], "The 22nd India–USA exercise Yudh Abhyas (2026) was held at Auli (Uttarakhand) and the Mahajan range (Rajasthan), not in Alaska.", k=1),
 P("Johannesburg (G20 2025)", [28.05, -26.20], "South Africa hosted the G20 leaders' summit in November 2025, the first in Africa.", c="South Africa"),
 P("Belém (COP30)", [-48.50, -1.46], "In northern Brazil, at the mouth of the Amazon. Hosted the UN climate conference COP30 in November 2025."),
 P("Bangkok (BIMSTEC 2025)", [100.50, 13.75], "Thailand hosted the 6th BIMSTEC summit in April 2025, which adopted the Bangkok Vision 2030.", c="Thailand"),
 P("Tianjin (SCO 2025)", [117.20, 39.13], "China hosted the SCO summit at Tianjin in late August and early September 2025.", k=1),
 P("Rio de Janeiro (BRICS 2025)", [-43.20, -22.90], "Brazil hosted the BRICS summit in July 2025. India holds the BRICS chair in 2026.", k=1),
 P("Uzbekistan (DUSTLIK)", [64.00, 41.50], "India and Uzbekistan hold the army exercise DUSTLIK. The 2026 edition was reported in Uzbekistan.", c="Uzbekistan", k=1),
 P("Mongolia (Nomadic Elephant)", [103.00, 46.50], "India and Mongolia hold the army exercise Nomadic Elephant. Mongolia also hosts the peacekeeping exercise Khaan Quest.", c="Mongolia"),
]),
]
