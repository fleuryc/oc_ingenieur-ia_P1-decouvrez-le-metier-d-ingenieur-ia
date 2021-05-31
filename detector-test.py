from detector import detect_language


texts = [
    {
        "value": "Philip Johnson architectural drawings, 1943-1994 (bulk 1943-1970).Held by the Department of Drawings & Archives, Avery Architectural & Fine Arts Library, Columbia University.",
        "language": "en",
    },
    {
        "value": "1910年~1915年任忠淸南道道伯，1915年中樞院贊議、1921年至1923年黃海道道知事、1923年至1925年忠淸北道道知事、1926年黃海道道知事、1936年中樞院顧問。1941年再任中樞院顧問、1943年10月中樞院副議長。1945年4月~8月日本帝國政府嗰特別任命，日本國貴族院議員。",
        "language": "zh-Hant",
    },
    {
        "value": "उद्यान आभा तूफ़ान एक्स्प्रेस 3007 भारतीय रेल द्वारा संचालित एक मेल एक्स्प्रेस ट्रेन है। यह ट्रेन हावड़ा जंक्शन रेलवे स्टेशन (स्टेशन कोड:HWH) से 09:45AM बजे छूटती है और मुग़ल सराय जंक्शन रेलवे स्टेशन (स्टेशन कोड:MGS) पर 02:15AM बजे पहुंचती है। इसकी यात्रा अवधि है 16 घंटे 30 मिनट।",
        "language": "hi",
    },
    {
        "value": "2014 debía de ser la temporada de la consagración de Elissonde, pero no fue así. Comenzó su temporada de nuevo en el Tour de Omán pero no repitió el éxito del año pasado, y esta vez fue 21.º en la clasificación general final. En el Tour de l'Ain en el que el año pasado se llevó la clasificación de los jóvenes, solo puso ser 13.º.",
        "language": "es",
    },
    {
        "value": "Les supporters de l'ASM Clermont Auvergne ont reçu en 2007, 2008 et 2009 le prix de l’Éthique et de la convivialité (challenge des meilleurs supporters) du Top 14.",
        "language": "fr",
    },
    {
        "value": 'كانت رحلة كوك - فولسوم - بيترسون الاستكشافية عام 1869م أول رحلة استكشافية مفصلة إلى منطقة يلوستون، وضمت الرحلة ثلاثة مستكشفين ممّولين من قِبَل القطاع الخاص وقد تبع فريق فولسوم نهر يلوستون إلى بحيرة يلوستون وقد احتفظ الأعضاء بمجلة واعتمدوا على المعلومات الواردة فيها. بعد ذلك نظّم فريق من سكان مونتانا رحلة واشبرن – لانغفورد - دُوان الاستكشافية عام 1870م. ترأسها مسّاح الأراضي العام لمونتانا هنري واشبرن بالإضافة إلى ناثانيل بي لانغفورد وكتيبة من الجيش الأمريكي بقيادة المُلازم غوستافوس دُوان لانغفورد الذي أصبح يعرف باسم "المنتزه الوطني". استغرقت الرحلة ما يُقارب الشهر في استكشاف المنطقة وجمع العينات وتسمية المواقع الهامة واقترح كاتب ومحامي في مونتانا يدعى كورنيليوس هِدقس وكان عضوًا في رحلة واشبرن الاستكشافية ضرورة وضع المنطقة جانبًا وحمايتها باعتبارها منتزهًا وطنيًا وقد كتب عددًا من المقالات المفصّلة لصحيفة هيلينا هيرالد بين 1870 و 1871 حول ملاحظاته.',
        "language": "ar",
    },
]

for text in texts:
    detected_language = detect_language(text["value"])
    if detected_language == text["language"]:
        print(f'Correct language detected : "{ detected_language }"')
    else:
        print(
            f'Wrong language detected : "{ detected_language }" instead of "{ text["language"] }"'
        )
