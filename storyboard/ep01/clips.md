# 1화 클립 목록과 프롬프트

- 모델: 시댄스 2.5 (힉스필드 `seedance_2_5`, `omni_reference`), 480p, 16:9, 소리 생성 켬
- 규칙: 한 클립 = 한 장소, 끊기지 않는 시간. 30초 이하. 대사는 클립당 6~8줄 이하.
- 자막("세종 16년…", "열여덟 시간 전")은 영상에 넣지 않고 편집에서 넣는다.
- `@Image N`은 참조 이미지를 넣는 순서다. 각 클립의 **참조** 목록 순서대로 넣는다.
- 클립 5-A는 `clip05a.md`에 따로 있다 (테이크 1 채택 후보).

## 클립 목록

| 클립 | 씬 | 장소 | 길이 | 등장 | 상태 |
|---|---|---|---|---|---|
| 01 | 1 | 성루, 밤 | 25초 | 한이겸, 천봉수, 군관들 | **테이크 1 생성** (`renders/ep01/clip01_take1.mp4`, job `4d3ee2e8-badf-4db8-894d-62148c119344`). 받아쓰기: "적이 육천입니다. 아군은 팔백입니다." 9초, "장정(장군?), 명을 내리소서." 15초. 한이겸이 시트의 철릭 대신 전신 찰갑을 입고 나옴(채택, 06A도 같은 갑옷). 속마음 3줄 합본: `renders/ep01/clip01_take1_vo.mp4` (1.5초 "여기 어디야…", 12초 "육천? 팔백? 재고 얘긴가", 18초 "장군? 나한테 하는 소리야?") |
| 02A | 2 | 물류센터 사무실 | 25초 | 박만수, 최 상무 | 프롬프트 완료 |
| 03 | 3 | 관리사무소 | 30초 | 박만수, 관리소장 | 프롬프트 완료 |
| 04 | 4 | 거실, 밤 | 30초 | 박만수, 정숙, 하은 | 프롬프트 완료 |
| 05A | 5 | 군막 | 30초 | 한이겸 | **생성 완료** |
| 05B | 5 | 군막 | 30초 | 한이겸, 천봉수 | 프롬프트 완료 |
| 06A | 6 | 성루, 아침 | 25초 | 한이겸, 천봉수, 조윤, 군관들 | 프롬프트 완료 |
| 06B | 6 | 지휘 군막 | 30초 | 한이겸, 천봉수, 조윤, 군관들 | 프롬프트 완료 |
| 06C | 6 | 지휘 군막 | 25초 | 한이겸, 천봉수, 조윤 | 프롬프트 완료 |
| 07A | 7 | 군량 창고 | 30초 | 한이겸, 천봉수, 조윤, 병사들 | 프롬프트 완료 |
| 07B | 7 | 군량 창고 | 25초 | 한이겸, 천봉수, 조윤 | 프롬프트 완료 |
| 08A | 8 | 거실, 아침 | 20초 | 박만수, 정숙 | 프롬프트 완료 |
| 08B | 8 | 현관 | 15초 | 박만수(경비복), 하은 | 프롬프트 완료 |

합계 약 6분 40초, 14클립.

## 생성 전에 만들어야 할 참조 이미지

| 종류 | 항목 | 상태 |
|---|---|---|
| 인물 시트 | 박만수, 한이겸, 천봉수, 조윤, 정숙, 하은 | 완료 |
| 인물 시트 | 최 상무, 관리소장 | **필요** |
| 의상 시트 | 박만수 경비복 | **필요** (08B) |
| 장소 | 군막 | 완료 (`docs/locations/tent_a.png`) |
| 장소 | 성루, 지휘 군막, 군량 창고, 물류센터 사무실, 물류센터 창고, 관리사무소, 거실(식탁·소파), 현관 | **필요** (8장) |

군관 여섯, 지게차 기사, 병사들은 시트 없이 프롬프트 묘사로 처리한다. 얼굴이 크게 나오지 않게 배치한다.

## 목소리 고정 문구

매 클립의 [Audio]에 해당 인물 문구를 글자 그대로 쓴다.

| 인물 | 문구 |
|---|---|
| 박만수 | `a warm, slightly husky baritone of a man in his fifties, speaking slowly and politely` |
| 한이겸 (1~2화) | `a deep young male voice, but with the hesitant, overly polite tone of a tired middle-aged office worker` |
| 천봉수 | `a loud, gruff, earnest voice of a stocky man in his forties` |
| 조윤 | `a smooth, soft, measured tenor, calm and courteous` |
| 정숙 | `a bright, brisk, warm voice of a woman in her forties` |
| 하은 | `a low, flat, tired voice of a woman in her late twenties` |
| 최 상무 | `a polished, smooth, businesslike voice of a man in his late forties` |
| 관리소장 | `a dry, slow, raspy voice of a man in his sixties` |

---

## 클립 01 — 성루, 밤 (25초)

**참조**: 1 한이겸 시트, 2 천봉수 시트, 3 성루

```
[Generation Goal]
A tense cold-open for a historical comedy-drama: on a fortress wall at night, a young Joseon general is asked for orders by his kneeling officers and cannot speak.

[Reference Material Roles]
@Image 1 defines Han Igyeom's face, hairstyle, build and clothing. Do not use the grey background or the panel layout.
@Image 2 defines Cheon Bongsu's face, hairstyle, build and clothing. Do not use the grey background or the panel layout.
@Image 3 defines the fortress wall walkway, crenellations and wooden gate tower. @Image 3 is a style reference only, not a fixed keyframe.

[Subjects and Relationships]
Han Igyeom corresponds to @Image 1 and wears a dark iron helmet in addition to his clothing. Cheon Bongsu corresponds to @Image 2. Han Igyeom stands at the crenellations facing outward over the plain; Cheon Bongsu kneels on one knee behind him on the walkway, with six officers in brown leather armor kneeling in a row behind Cheon Bongsu, their faces lowered. The top of Cheon Bongsu's head reaches only Han Igyeom's nose.

[Event Script]
Stage 1 - The plain: Opening state: snow falls at night. Beyond the wall, thousands of torches spread across the dark plain to the horizon. End state: the camera settles behind Han Igyeom's shoulder looking out at the torches.
Stage 2 - The report: Han Igyeom grips the stone crenellation with both hands; his fingers tremble. Cheon Bongsu kneels and says firmly in Korean, {적이 육천입니다. 아군은 팔백입니다.} Han Igyeom swallows hard. End state: Han Igyeom stays facing the plain.
Stage 3 - The order: Cheon Bongsu lifts his head and says in Korean, {장군, 명을 내리소서.} Han Igyeom turns his head toward the officers, opens his mouth, and no sound comes out. End state: a close-up of his frozen, open-mouthed face, held still until the clip ends.

[Visual and Camera Treatment]
Stage 1 opens on a wide shot from the wall over the torch-filled plain, then cranes down behind Han Igyeom's shoulder. Stage 2 is a medium shot from the side with the kneeling officers visible behind him. Stage 3 pushes in to a close-up of Han Igyeom's face. Cold blue night light, warm torchlight flickering from the wall's braziers on the right.

[Audio]
<wind>, <distant war drums from the plain>, <torches crackling>. Cheon Bongsu speaks Korean in a loud, gruff, earnest voice of a stocky man in his forties. Only Cheon Bongsu speaks. The clip ends in sudden silence.

[Maintain Consistency]
Keep Han Igyeom's and Cheon Bongsu's faces and clothing identical to their references; keep the plain on the outer side of the wall and the officers behind Han Igyeom.
```

## 클립 02A — 물류센터 사무실, 낮 (25초)

**참조**: 1 박만수 시트, 2 최 상무 시트, 3 물류센터 사무실

```
[Generation Goal]
A quiet office scene in a modern workplace: a fifty-four-year-old warehouse manager pleads for one more year with his former subordinate, now an executive, before signing his resignation paper and surrendering his locker key.

[Reference Material Roles]
@Image 1 defines Park Mansu's face, hairstyle, build and clothing. Do not use the grey background or the panel layout.
@Image 2 defines Executive Choi's face, hairstyle, build and clothing. Do not use the grey background or the panel layout.
@Image 3 defines the logistics center office interior with an office desk, chairs, and a wide glass wall overlooking the warehouse floor. @Image 3 is a style reference only, not a fixed keyframe.

[Subjects and Relationships]
Park Mansu corresponds to @Image 1 and wears a locker key on a cord around his neck in addition to his clothing. Executive Choi corresponds to @Image 2. The two sit facing each other across the office desk in front of the interior glass wall, with Park Mansu on the left and Executive Choi on the right. On the desk between them lie a single printed resignation document and a ballpoint pen. Beyond the glass wall behind them, forklifts move back and forth along the warehouse aisles.

[Event Script]
Stage 1 - The plea: Opening state: forklifts pass beyond the glass wall while Park Mansu sits looking down at the document and ballpoint pen on the desk and Executive Choi sits across from him. Executive Choi hesitates over the form of address and says in Korean, {부장님… 아니, 선배님. 저도 마음이 안 좋습니다.} Park Mansu raises his eyes to Executive Choi and begins to speak; as he slips into calling him by his old rank of Assistant Manager Choi, Park Mansu pauses abruptly and winces to correct himself while Executive Choi stiffens with an awkward, strained expression, and Park Mansu pleads earnestly in Korean, {최 대리… 아, 상무님. 우리 애 취직할 때까지만요. 일 년만.} End state: Park Mansu leans slightly forward across the desk, looking at Executive Choi, whose face remains tense and awkward.
Stage 2 - The hesitation: Executive Choi answers calmly in Korean, {본사 결재가 어제 끝났어요.} Park Mansu lowers his gaze, picks up the ballpoint pen, sets it back down on the desk, and picks it up again. End state: Park Mansu holds the pen still above the signature line of the document.
Stage 3 - Twenty-seven years: Looking down at the paper, Park Mansu says quietly in Korean, {제가 여기서 이십칠 년입니다.} Executive Choi replies evenly in Korean, {그래서 위로금도 넉넉히 넣었습니다.} End state: Park Mansu presses his lips together and lowers the tip of the pen to the paper.
Stage 4 - The signature and key: Park Mansu signs his name on the document, lifts the locker key cord over his head, and places the key on top of the signed paper. End state: a close shot holds still on the signed document with the locker key resting on top of it as Park Mansu's hand pulls back.

[Visual and Camera Treatment]
Stage 1 opens on a medium two-shot from the side across the desk at eye level, with the glass wall and moving forklifts visible in the background, and cuts to medium close-ups showing Park Mansu faltering as he corrects the title and Executive Choi's awkward expression. Stage 2 cuts to a medium close-up on Park Mansu and his hand picking up and setting down the pen. Stage 3 alternates between medium close-ups of Park Mansu and Executive Choi over each shoulder. Stage 4 tilts down to a close-up of the document and locker key on the desk. Cool fluorescent ceiling light overhead mixes with soft daylight coming from the warehouse floor through the glass wall behind them.

[Audio]
<faint hum of forklifts beyond the glass>, <pen clicking against the desk>, <pen scratching on paper>, <metal locker key clinking softly on paper>. Park Mansu speaks Korean in a warm, slightly husky baritone of a man in his fifties, speaking slowly and politely. Executive Choi speaks Korean in a polished, smooth, businesslike voice of a man in his late forties.

[Maintain Consistency]
Keep Park Mansu's and Executive Choi's faces and clothing identical to their references; keep Park Mansu on the left of the desk, Executive Choi on the right, and the glass wall to the warehouse behind them.
```

## 클립 03 — 관리사무소 (30초)

**참조**: 1 박만수 시트, 2 관리소장 시트, 3 관리사무소

```
[Generation Goal]
Live-action Korean comedy drama, real-time natural speed: in a cramped apartment management office, a laid-off warehouse manager in his fifties interviews for a night security guard job, names inventory checking as his special skill, and is hired on the spot to sort a mountain of cardboard boxes. The camera stays at seated eye level.

[Reference Material Roles]
@Image 1 defines only Park Mansu's face, hairstyle, build and clothing. Do not copy its framing, grey background or panel layout.
@Image 2 defines only the Office Manager's face, hairstyle, build and clothing. Do not copy its framing, grey background or panel layout.
@Image 3 defines only the management office's furniture, walls and light: the worn wooden desk with a cream desk fan, the black leather desk chair, the metal folding chair, the whiteboard duty roster, and the window behind the desk overlooking a recycling yard piled with cardboard. @Image 3 is a style reference only, not a fixed keyframe.

[Subjects and Relationships]
Park Mansu corresponds to @Image 1: an original 54-year-old Korean man, broad-shouldered sturdy build with a slight belly, short neatly combed salt-and-pepper hair grey at the temples, one small dark mole on the left cheekbone just below the left eye, wearing a charcoal grey zip-up padded work jacket over a navy blue polo shirt, dark grey slacks, and a cheap silver wristwatch on the left wrist.
The Office Manager corresponds to @Image 2: an original 63-year-old Korean man, thin and slightly stooped, thinning grey hair combed over to one side, thick black-framed reading glasses resting low on his nose, wearing a navy blue quilted work vest with a small name tag over a beige checked flannel shirt.
The Office Manager always sits in the black leather chair on the inner side of the desk with his back to the window; the cardboard mountain in the recycling yard stays visible through the window behind his shoulders. Park Mansu always sits on the metal folding chair on the outer side of the desk, facing the Office Manager across it, back straight, both hands flat on his knees. The cream desk fan sits on the desk corner between them, swivelling left and right.

[Event Script]
0-3s: Medium two-shot from the side of the desk. The Office Manager holds a one-page printed résumé in both hands and reads it over the top of his reading glasses. Park Mansu sits upright on the folding chair, hands on his knees, waiting. Both mouths closed.
3-6s: Medium close-up of the Office Manager, eyes on the résumé. At 3s he says in Seoul-accented Korean, in a flat, dry tone: {쉰넷. 나이가 좀 많으시네.}
6-8s: Medium close-up of Park Mansu. He straightens his back. At 6s he says in Seoul-accented Korean, firm and sincere: {체력은 자신 있습니다.}
8-12s: Medium close-up of the Office Manager, résumé still in both hands. At 8s he says in Seoul-accented Korean, flat and unhurried: {물류센터 부장을 하셨네. 경비 일은 해 보셨어요?}
12-14s: Medium close-up of Park Mansu. Lips pressed together, he gives a small, honest shake of his head. His mouth stays closed.
14-16s: Medium close-up of the Office Manager. At 14s he says in Seoul-accented Korean, flat: {그럼 특기가 뭡니까?}
16-18s: Close-up of Park Mansu, eyes earnest and steady. At 16s he says in Seoul-accented Korean, completely serious: {재고 조사입니다.}
18-21s: The key moment. Starting from a medium close-up of the Office Manager, the camera dollies in across this whole range to a tight close-up of his eyes. Hearing the answer, he lowers the résumé to the desk, then with one finger pushes his reading glasses down to the tip of his nose and looks straight into Park Mansu's face over the black frames. The fan's breeze lifts a corner of the paper. Mouth closed, face blank.
21-22s: Same tight close-up, camera locked off. At 21s the Office Manager repeats in Seoul-accented Korean, flat as a board: {재고 조사.}
22-25s: Medium close-up of Park Mansu, camera locked off. He leans in a little. At 22s he says in Seoul-accented Korean, earnest and sincere: {숫자하고 물건이 안 맞으면 잠이 안 옵니다.}
25-28s: Medium two-shot from the side of the desk, camera locked off. Keeping his eyes on Park Mansu, the Office Manager jabs his thumb back over his shoulder toward the window and the cardboard mountain behind him. At 25s he says in Seoul-accented Korean, flat: {저거나 좀 맞춰 봐요. 내일부터 야간입니다.}
28-30s: Same two-shot, camera locked off. Park Mansu glances at the window, stands up from the folding chair, and bows deeply from the waist toward the Office Manager, hands at his sides. Final frame: Park Mansu held in the deep bow beside the desk while the Office Manager has the résumé back up in front of his face.

[Visual and Camera Treatment]
All shots at seated eye level, from the folding-chair side of the action line. Camera on a tripod and locked off in every shot except the dolly-in at 18-21s. Faces fill a large part of the frame in every shot. Lighting for this location: warm low afternoon sun through the window behind the desk lays bright stripes across the desk top, with one bare fluorescent tube overhead giving a flat greenish fill.

[Audio]
No BGM; only ambient and action sounds: <the desk fan's steady whir and soft rattle as it swivels>, <paper rustling>, <a dry creak of the leather chair>, <the folding chair scraping as Park Mansu stands>, <jacket nylon rustling on the bow>. At 18-21s only the fan is heard. Park Mansu speaks Korean in a warm, slightly husky baritone of a man in his fifties, speaking slowly and politely. The Office Manager speaks Korean in a dry, slow, raspy voice of a man in his sixties. Only the man speaking in each shot moves his mouth; the other man keeps his mouth closed.

[Maintain Consistency]
@Image 1 is Park Mansu, @Image 2 is the Office Manager, @Image 3 is the office. Keep both men's faces, hair and clothing identical to their references, the reading glasses on the Office Manager's nose, the Office Manager behind the desk with the window and cardboard mountain behind him, Park Mansu on the folding chair across the desk, and the camera on the folding-chair side of the action line. Normal human eyes. Real-time natural speed, no slow motion. No subtitles, no on-screen text.
```

## 클립 04 — 거실, 밤 (30초)

**참조**: 1 박만수 시트, 2 정숙 시트, 3 하은 시트, 4 거실

```
[Generation Goal]
Live-action Korean family drama, real-time natural speed: in an apartment dining area and living room at night, a laid-off father in his fifties tries and fails to tell his wife and daughter that he lost his job over dinner, then falls asleep on the sofa in front of a period drama on television. The camera stays at seated eye level.

[Reference Material Roles]
@Image 1 defines only Park Mansu's face, hairstyle, build and clothing. Do not copy its framing, grey background or panel layout.
@Image 2 defines only Jeongsuk's face, hairstyle, build and clothing. Do not copy its framing, grey background or panel layout.
@Image 3 defines only Haeun's face, hairstyle, build and clothing. Do not copy its framing, grey background or panel layout.
@Image 4 defines only the apartment living room's furniture, walls and light: the dining table with chairs, the living room sofa, the television set, and the bedroom door behind the dining area. @Image 4 is a style reference only, not a fixed keyframe.

[Subjects and Relationships]
Park Mansu corresponds to @Image 1: an original 54-year-old Korean man, broad-shouldered sturdy build with thick forearms and a slight belly, short, thick, neatly trimmed salt-and-pepper hair, grey at the temples, combed back neatly, one small dark mole on the left cheekbone just below the left eye, wearing a charcoal grey zip-up padded work jacket in matte nylon over a navy blue polo shirt with the collar visible, dark grey slacks, and a cheap silver wristwatch on the left wrist.
Jeongsuk corresponds to @Image 2: an original 52-year-old Korean woman, slim and well-kept figure, shoulder-length dark brown hair with soft loose waves, glossy and neatly styled with a side part, small pearl stud earrings, wearing a soft cream knit cardigan over a light blue and white striped cotton blouse, dark brown cotton trousers, a navy blue apron printed with small white flowers tied at the waist, and a thin plain gold wedding ring.
Haeun corresponds to @Image 3: an original 27-year-old Korean woman, slim build, faint dark circles under the eyes, one small dark mole just above the right side of the upper lip, long straight black hair worn loose with a center part, falling past the shoulders, wearing an oversized heather grey hoodie, black jogger pants, and small silver stud earrings.
The top of Jeongsuk's head reaches Park Mansu's nose. The top of Haeun's head reaches Park Mansu's nose. Jeongsuk and Haeun are about the same height.
At the dining table, Park Mansu always sits at the head of the table holding a metal spoon in his right hand; Jeongsuk always sits on his left side with an open household ledger and paper receipts on the tabletop in front of her; Haeun sits on his right side holding a smartphone in her left hand with her rice bowl in front of her until she exits through the bedroom door in the background. A bubbling earthenware pot of doenjang stew always sits in the center of the dining table between them. In the living room area, the sofa always faces the television set.

[Event Script]
0-3s: Medium two-shot at seated eye level across the corner of the dining table, framing Park Mansu at the head of the table and Jeongsuk on his left with the bubbling pot of doenjang stew in the foreground. Jeongsuk presses a paper receipt into her open household ledger while Park Mansu holds his metal spoon and shifts his gaze from Jeongsuk toward Haeun's side on his right. Both mouths closed.
3-5s: Medium close-up of Park Mansu at the head of the table, metal spoon held in his right hand. He leans forward a little. At 3s he says in Seoul-accented Korean, in a hesitant, low tone: {저기, 내가 할 말이.}
5-9s: Medium close-up of Jeongsuk at the left side of the table, with the open household ledger and paper receipts filling the foreground on the tabletop under her hands. Keeping her eyes down on the ledger, she smooths a receipt onto the page. At 5s she says in Seoul-accented Korean, in a brisk, worried tone: {여보, 이번 달 대출 이자 또 올랐어.}
9-12s: Medium close-up of Park Mansu. Hearing her words, he presses his lips together with his spoon held still above the table, then turns his head toward Haeun on his right. At 10s he says in Seoul-accented Korean, in a careful, warm tone: {하은아, 면접은.}
12-15s: Medium close-up of Haeun at the right side of the table, her rice bowl on the tabletop and her smartphone held up in front of her chest as she looks at the phone screen. At 12s she says in Seoul-accented Korean, in a flat, indifferent tone: {아빠는 몰라도 돼.}
15-17s: Medium two-shot from the front corner of the dining table showing Haeun on the right and Park Mansu at the head. Haeun rises from her chair carrying her rice bowl and smartphone, steps into the bedroom doorway behind the table, and pulls the door shut behind her while Park Mansu looks at her empty chair. Both mouths closed.
17-19s: Medium close-up of Jeongsuk with the open household ledger in front of her. She lifts her eyes from the ledger toward Park Mansu. At 17s she says in Seoul-accented Korean, in a warm, casual tone: {회사는 별일 없지?}
19-23s: The key moment. Starting from a medium close-up of Park Mansu with the bubbling pot of doenjang stew clearly visible in the foreground on the table, the camera dollies in across this whole range to a tight close-up of his face. He dips his metal spoon into the pot of doenjang stew, lifts a full spoonful, and forms a faint, reassuring smile toward Jeongsuk. At 20s he says in Seoul-accented Korean, in a calm, even tone: {별일 없지.}
23-26s: Over-the-shoulder medium shot from beside Park Mansu on the living room sofa toward the glowing television screen, with the black remote control visible in Park Mansu's right hand in the foreground. On the television screen, a bearded actor in Joseon general armor draws a long sword and raises it high. At 23s the actor on the television screen shouts in Seoul-accented Korean, in a booming theatrical tone: {전군, 나를 따르라!} Park Mansu's mouth stays closed.
26-30s: Medium close-up of Park Mansu on the living room sofa, camera locked off. With the television remote held in his right hand on his lap, his eyelids close, his chin drops onto his chest, and his mouth parts in a steady snore under the flickering blue television glow. Final frame: Park Mansu held asleep on the sofa with his head drooped, the remote in his hand, and blue television light flickering across his face.

[Visual and Camera Treatment]
All shots at seated eye level, staying on the front side of the dining table and the television side of the living room sofa along a single action line. Camera on a tripod and locked off in every shot except the dolly-in at 19-23s. Faces fill a large part of the frame in every shot, starting from a medium two-shot and moving into medium close-ups and close-ups. Lighting for this location: warm overhead pendant light illuminates the dining table and faces during dinner, while the living room sofa area is lit by the flickering blue glow of the television screen against soft warm apartment wall light.

[Audio]
No BGM; only ambient and action sounds: <soft bubbling of doenjang stew>, <paper receipt rustling against the ledger>, <metal spoon clinking against the bowl>, <wooden chair scraping softly>, <bedroom door clicking shut>, <sword-draw ring from the television speaker>, <Park Mansu's steady snoring>. Park Mansu speaks Korean in a warm, slightly husky baritone of a man in his fifties, speaking slowly and politely. Jeongsuk speaks Korean in a bright, brisk, warm voice of a woman in her forties. Haeun speaks Korean in a low, flat, tired voice of a woman in her late twenties. The television general speaks Korean in a booming, commanding theatrical male voice. Only the person speaking in each shot moves their mouth; everyone else keeps their mouth closed.

[Maintain Consistency]
@Image 1 is Park Mansu, @Image 2 is Jeongsuk, @Image 3 is Haeun, @Image 4 is the apartment living room and dining area. Keep Park Mansu's, Jeongsuk's, and Haeun's faces, hair and clothing identical to their references, including Park Mansu's charcoal grey work jacket and cheap silver wristwatch, Jeongsuk's navy floral apron and pearl stud earrings, and Haeun's oversized heather grey hoodie. Keep Park Mansu at the head of the dining table, Jeongsuk on his left with the household ledger and receipts, Haeun on his right with her smartphone and rice bowl until she exits through the bedroom door, the pot of doenjang stew in the center of the table, and the camera on the front side of the action line. Normal human eyes. Real-time natural speed, no slow motion. No subtitles, no on-screen text.
```

## 클립 05B — 군막 (30초)

**참조**: 1 한이겸 시트, 2 천봉수 시트, 3 군막 (`tent_a.png`)

```
[Generation Goal]
A comedic scene: a general who is secretly a modern office worker speaks to his loyal officer in polite modern Korean, and the officer is baffled.

[Reference Material Roles]
@Image 1 defines Han Igyeom's face, hairstyle, build and clothing. Do not use the grey background or the panel layout.
@Image 2 defines Cheon Bongsu's face, hairstyle, build and clothing. Do not use the grey background or the panel layout.
@Image 3 defines the tent interior: canvas walls, wooden pillars, sleeping platform, brass washbasin, oil lamp, armor stand. @Image 3 is a style reference only, not a fixed keyframe.

[Subjects and Relationships]
Han Igyeom corresponds to @Image 1; Cheon Bongsu corresponds to @Image 2. Han Igyeom sits on the edge of the sleeping platform next to the brass washbasin. Cheon Bongsu enters through the tent flap on the right and stands in front of him. The top of Cheon Bongsu's head reaches only Han Igyeom's nose, so when Han Igyeom stands, Cheon Bongsu looks up at him.

[Event Script]
Stage 1 - The entrance: Cheon Bongsu pushes aside the tent flap and says in Korean, {장군, 기침하셨습니까.} Han Igyeom hurriedly hides the washbasin behind his back and asks politely in Korean, {저, 실례지만 어디서 오셨어요?} Cheon Bongsu freezes. End state: Cheon Bongsu stands stiff, eyes wide.
Stage 2 - Wrong speech: Cheon Bongsu says in Korean, {장군, 어찌 소인한테 존대를 하십니까?} Han Igyeom fumbles, trying different endings, in Korean, {아, 그러니까. 그대는, 누구시, 누구시오. 누구냐.} With every attempt, Cheon Bongsu's eyes grow wider. End state: Cheon Bongsu blinks rapidly.
Stage 3 - The forehead: Cheon Bongsu says in Korean, {군관 천봉수입니다. 십 년을 모셨습니다.} He reaches up and presses the back of his hand to Han Igyeom's forehead and says in Korean, {열은 없으신데, 말씀이 영 이상하십니다.} Outside, the drumbeat speeds up. End state: Cheon Bongsu turns his head toward the sound.
Stage 4 - The helmet: Cheon Bongsu says in Korean, {적이 진을 쳤습니다. 성루로 가셔야 합니다.} He holds out an iron helmet. Han Igyeom takes it and puts it on backwards. Without a word, Cheon Bongsu reaches up and turns it around. End state: hold on the two of them, Han Igyeom wearing the helmet correctly and Cheon Bongsu staring at him.

[Visual and Camera Treatment]
Medium two-shot at eye level from the side, with quick close-ups on Cheon Bongsu's widening eyes in Stage 2. Warm oil-lamp light from the left, cold blue dawn light through the open tent flap on the right.

[Audio]
<war drum outside, slow then faster>, <armor creaking>. Han Igyeom speaks Korean in a deep young male voice, but with the hesitant, overly polite tone of a tired middle-aged office worker. Cheon Bongsu speaks Korean in a loud, gruff, earnest voice of a stocky man in his forties.

[Maintain Consistency]
Keep both faces and clothing identical to their references; keep the tent flap on the right and the lamp light from the left; Cheon Bongsu stays clearly shorter than Han Igyeom.
```

## 클립 06A — 성루, 아침 (25초)

**참조**: 1 한이겸 시트, 2 천봉수 시트, 3 조윤 시트, 4 성루

```
[Generation Goal]
A comedic beat on a fortress wall at dawn: officers await battle orders, and their general proposes "a meeting".

[Reference Material Roles]
@Image 1 defines Han Igyeom's face, hairstyle, build and clothing. Do not use the grey background or the panel layout.
@Image 2 defines Cheon Bongsu's face, hairstyle, build and clothing. Do not use the grey background or the panel layout.
@Image 3 defines Jo Yun's face, hairstyle, build and clothing. Do not use the grey background or the panel layout.
@Image 4 defines the fortress wall walkway, crenellations and gate tower. @Image 4 is a style reference only, not a fixed keyframe.

[Subjects and Relationships]
Han Igyeom corresponds to @Image 1 and wears an iron helmet. Cheon Bongsu corresponds to @Image 2. Jo Yun corresponds to @Image 3. Han Igyeom stands at the crenellations; Cheon Bongsu and six officers in brown leather armor stand in a half circle facing him; Jo Yun stands one step behind them with his hands tucked into his sleeves. Beyond the wall, enemy tents stretch across a snowy plain in the morning light. The top of Cheon Bongsu's head reaches only Han Igyeom's nose.

[Event Script]
Stage 1 - The question again: Cheon Bongsu says in Korean, {적이 육천입니다. 아군은 팔백입니다. 장군, 명을 내리소서.} The officers look up at Han Igyeom. End state: all eyes on him.
Stage 2 - The meeting: Han Igyeom grips the crenellation, looks at the officers, at the plain, and back at the officers. He says in Korean, {일단 회의부터 합시다.} The officers exchange glances. Cheon Bongsu says in Korean, {장군, 저희한테 '합시다'라니요. 그리고 회의가 무엇입니까?} End state: Cheon Bongsu waits, frowning.
Stage 3 - Explaining: Han Igyeom says, correcting himself twice, in Korean, {다 같이 앉아서 얘기하는 거예요. 거요. 거다.} Behind the officers, Jo Yun's faint half-smile does not move, but his eyes narrow slightly. End state: hold on Jo Yun watching.

[Visual and Camera Treatment]
Stage 1 is a medium shot from behind the officers toward Han Igyeom with the plain beyond the wall. Stage 2 cuts to a medium close-up of Han Igyeom, then to the officers' faces. Stage 3 ends on a close-up of Jo Yun. Cold, clear morning light from the left, snow glare from the plain.

[Audio]
<wind>, <distant enemy horns>. Han Igyeom speaks Korean in a deep young male voice, but with the hesitant, overly polite tone of a tired middle-aged office worker. Cheon Bongsu speaks Korean in a loud, gruff, earnest voice of a stocky man in his forties.

[Maintain Consistency]
Keep all three faces and clothing identical to their references; keep the plain on the outer side of the wall and Jo Yun behind the officers.
```

## 클립 06B — 지휘 군막, 회의 (30초)

**참조**: 1 한이겸 시트, 2 천봉수 시트, 3 조윤 시트, 4 지휘 군막

```
[Generation Goal]
A comedic first "meeting" in a Joseon command tent: stiff officers sit around a table, gossip about their strange general, and the general asks for the grain ledger.

[Reference Material Roles]
@Image 1 defines Han Igyeom's face, hairstyle, build and clothing. Do not use the grey background or the panel layout.
@Image 2 defines Cheon Bongsu's face, hairstyle, build and clothing. Do not use the grey background or the panel layout.
@Image 3 defines Jo Yun's face, hairstyle, build and clothing. Do not use the grey background or the panel layout.
@Image 4 defines the large command tent with a long low wooden table and floor cushions. @Image 4 is a style reference only, not a fixed keyframe.

[Subjects and Relationships]
Han Igyeom corresponds to @Image 1 and sits at the head of the long table, helmet removed beside him. Cheon Bongsu corresponds to @Image 2 and sits at Han Igyeom's right hand. Jo Yun corresponds to @Image 3 and sits at Han Igyeom's left hand with a bound ledger under his hand. Four officers in brown leather armor sit down the sides of the table, backs stiff. Two of them, one young and thin, one older with a grey beard, sit side by side at the far end.

[Event Script]
Stage 1 - Stiff: The officers sit with unnaturally straight backs, hands on their knees. At the far end, the young officer leans to the grey-bearded officer and whispers in Korean, {장군 말씀이 왜 저러시나.} The grey-bearded officer whispers back in Korean, {어젯밤에 말에서 떨어지셨다던데.} End state: both are still leaning together.
Stage 2 - Caught: Han Igyeom turns and looks straight at them. Both instantly snap upright at the same moment. End state: they stare straight ahead.
Stage 3 - The ledger: Han Igyeom asks in Korean, {먼저 현황부터. 쌀이 얼마나 남았소?} Jo Yun answers smoothly in Korean, {삼백 석입니다. 넉 달은 버팁니다.} Han Igyeom says in Korean, {장부 좀 봅시다.} Jo Yun pauses for a beat, then slides the ledger across the table. End state: Han Igyeom opens the ledger.

[Visual and Camera Treatment]
Stage 1 is a medium shot down the table toward the whispering pair. Stage 2 is a quick cut to Han Igyeom's look, then back to the pair snapping upright. Stage 3 is a medium shot of Han Igyeom and Jo Yun, ending on an insert of the ledger sliding across the wood. Warm lamp light inside the tent, daylight glowing through the canvas.

[Audio]
<armor creaking as officers shift>, <wind against the canvas>. The young officer whispers in a nervous young male voice; the grey-bearded officer whispers in an old, hoarse male voice. Han Igyeom speaks Korean in a deep young male voice, but with the hesitant, overly polite tone of a tired middle-aged office worker. Jo Yun speaks Korean in a smooth, soft, measured tenor, calm and courteous.

[Maintain Consistency]
Keep Han Igyeom, Cheon Bongsu and Jo Yun identical to their references; keep Cheon Bongsu on Han Igyeom's right and Jo Yun on his left.
```

## 클립 06C — 지휘 군막, 장부 (25초)

**참조**: 1 한이겸 시트, 2 천봉수 시트, 3 조윤 시트, 4 지휘 군막

```
[Generation Goal]
A quiet tense beat: a general who was a warehouse manager in another life reads a grain ledger and spots that one person signed everything.

[Reference Material Roles]
@Image 1 defines Han Igyeom's face, hairstyle, build and clothing. Do not use the grey background or the panel layout.
@Image 2 defines Cheon Bongsu's face, hairstyle, build and clothing. Do not use the grey background or the panel layout.
@Image 3 defines Jo Yun's face, hairstyle, build and clothing. Do not use the grey background or the panel layout.
@Image 4 defines the command tent with the long low wooden table. @Image 4 is a style reference only, not a fixed keyframe.

[Subjects and Relationships]
Same seating as before: Han Igyeom at the head of the table with the open ledger, Cheon Bongsu at his right, Jo Yun at his left. The ledger pages are columns of handwritten classical Chinese characters with red seal-like signature marks at the end of each line.

[Event Script]
Stage 1 - Reading: Han Igyeom turns the pages and runs his finger down a column, line by line, like checking an invoice. His finger stops on one line. He says in Korean, {지난달에 이백 석이 들어왔는데, 나간 건 오십 석이네.} Jo Yun says in Korean, {그렇습니다.} Han Igyeom says in Korean, {그 전에 남은 게 백오십 석. 합치면 삼백 석. 숫자는 맞소.} Jo Yun's shoulders relax slightly. End state: Han Igyeom keeps his finger on the page.
Stage 2 - The signature: Han Igyeom taps the signature marks one after another and says in Korean, {그런데 받은 사람 수결이 석 달째 한 사람 글씨요.} Inside his sleeve, Jo Yun's hand closes into a fist. End state: Han Igyeom closes the ledger.
Stage 3 - Let's go: Han Igyeom stands and says in Korean, {입고하는 사람하고 확인하는 사람이 같으면 안 되지. 창고 갑시다.} Cheon Bongsu looks up at him and says in Korean, {지금 말입니까? 적이 코앞인데.} Han Igyeom says in Korean, {그러니까 지금 세야지.} End state: hold on Han Igyeom standing, Cheon Bongsu staring up at him.

[Visual and Camera Treatment]
Stage 1 is an insert of the finger moving down the ledger, then a medium close-up of Han Igyeom. Stage 2 includes a close-up of Jo Yun's sleeve as his hand tightens. Stage 3 is a low-angle medium shot of Han Igyeom standing, with Cheon Bongsu in the foreground. Warm lamp light.

[Audio]
<pages turning>, <wind against canvas>. Han Igyeom speaks Korean in a deep young male voice, but with the hesitant, overly polite tone of a tired middle-aged office worker, growing more confident with numbers. Jo Yun speaks Korean in a smooth, soft, measured tenor, calm and courteous. Cheon Bongsu speaks Korean in a loud, gruff, earnest voice of a stocky man in his forties.

[Maintain Consistency]
Keep all three faces and clothing identical to their references; keep Cheon Bongsu on Han Igyeom's right and Jo Yun on his left.
```

## 클립 07A — 군량 창고, 세기 (30초)

**참조**: 1 한이겸 시트, 2 천봉수 시트, 3 조윤 시트, 4 군량 창고

```
[Generation Goal]
A comedic reveal: soldiers restack the grain sacks in a fortress storehouse and discover that most of the grain is missing.

[Reference Material Roles]
@Image 1 defines Han Igyeom's face, hairstyle, build and clothing. Do not use the grey background or the panel layout.
@Image 2 defines Cheon Bongsu's face, hairstyle, build and clothing. Do not use the grey background or the panel layout.
@Image 3 defines Jo Yun's face, hairstyle, build and clothing. Do not use the grey background or the panel layout.
@Image 4 defines the dim wooden grain storehouse with straw rice sacks stacked along the walls. @Image 4 is a style reference only, not a fixed keyframe.

[Subjects and Relationships]
Han Igyeom stands in the middle of the storehouse floor; Cheon Bongsu stands at his right holding the ledger and a brush; Jo Yun stands near the door with his hands in his sleeves. Several soldiers in plain grey cotton uniforms carry sacks. From the front, the sacks along the walls look piled to the ceiling.

[Event Script]
Stage 1 - The order: Han Igyeom says in Korean, {한 줄에 열 섬씩. 줄 맞춰 다시 쌓으시오.} Soldiers start pulling sacks from the front of the pile. Behind the front row, the wall is bare and empty. The soldiers murmur. End state: a soldier holds a sack, staring at the empty space behind it.
Stage 2 - Counting: The sacks now lie on the floor in neat rows of ten. Cheon Bongsu walks along the rows pointing with his finger and counts in Korean, {열, 열하나, 열둘. 열두 줄입니다.} Han Igyeom says in Korean, {백이십 석.} Cheon Bongsu strikes a line through a number in the ledger with the brush and writes beside it. He says in Korean, {백여든 석이 빕니다.} End state: all the officers turn to look at Jo Yun.
Stage 3 - The rats: Jo Yun, expressionless, says in Korean, {쥐가 들었나 봅니다.} Han Igyeom says flatly in Korean, {쥐가 백여든 석을 먹으면 소만 해졌겠소.} A young soldier bursts out laughing and claps his hand over his mouth. End state: hold on the soldier with his hand over his mouth.

[Visual and Camera Treatment]
Stage 1 is a medium shot of the soldiers pulling sacks, revealing the empty wall. Stage 2 is a high-angle shot over the rows of sacks, then an insert of the brush on the ledger. Stage 3 cuts between Jo Yun's close-up, Han Igyeom's medium close-up and the laughing soldier. Shafts of dusty daylight through gaps in the wooden walls.

[Audio]
<straw sacks thudding>, <murmuring soldiers>, <a stifled laugh>. Han Igyeom speaks Korean in a deep young male voice, but with the hesitant, overly polite tone of a tired middle-aged office worker. Cheon Bongsu speaks Korean in a loud, gruff, earnest voice of a stocky man in his forties. Jo Yun speaks Korean in a smooth, soft, measured tenor, calm and courteous.

[Maintain Consistency]
Keep all three faces and clothing identical to their references; keep the counted sacks in neat rows of ten on the floor.
```

## 클립 07B — 군량 창고, 대호의 도착 (25초)

**참조**: 1 한이겸 시트, 2 천봉수 시트, 3 조윤 시트, 4 군량 창고

```
[Generation Goal]
A comic cliffhanger: the suspicious secretary quietly challenges the general, then the dreaded commander arrives for an inspection at the worst possible moment.

[Reference Material Roles]
@Image 1 defines Han Igyeom's face, hairstyle, build and clothing. Do not use the grey background or the panel layout.
@Image 2 defines Cheon Bongsu's face, hairstyle, build and clothing. Do not use the grey background or the panel layout.
@Image 3 defines Jo Yun's face, hairstyle, build and clothing. Do not use the grey background or the panel layout.
@Image 4 defines the dim wooden grain storehouse. @Image 4 is a style reference only, not a fixed keyframe.

[Subjects and Relationships]
Han Igyeom stands in the middle of the storehouse among the counted rows of sacks. Jo Yun stands close in front of him. Cheon Bongsu stands a few steps to Han Igyeom's right with two officers in brown leather armor. The top of Jo Yun's head reaches Han Igyeom's eyebrows.

[Event Script]
Stage 1 - The question: Jo Yun steps close to Han Igyeom and says quietly in Korean, {장군께서 언제부터 셈에 그리 밝으셨습니까.} A bead of sweat forms on Han Igyeom's temple. End state: they hold each other's gaze.
Stage 2 - The horn: A horn blasts outside. A soldier's voice shouts from outside in Korean, {기병이다! 성문으로 온다!} The officers grip their sword hilts. A beat later the voice shouts in Korean, {아니다! 우리 깃발이다! 도절제사 영감이시다!} The officers' faces go pale. End state: Cheon Bongsu hurries to Han Igyeom's side.
Stage 3 - The inspection: Cheon Bongsu whispers urgently up to Han Igyeom in Korean, {장군, 대호께서 오셨습니다. 하필 오늘.} Han Igyeom looks back at the empty wall behind the sacks and squeezes his eyes shut. He mutters in Korean, {본사 감사가 왜 하필 지금.} End state: hold on Han Igyeom's eyes squeezed shut.

[Visual and Camera Treatment]
Stage 1 is a tight two-shot of Jo Yun and Han Igyeom in profile, then a close-up of the sweat bead. Stage 2 is a medium shot of the officers turning toward the door, light flaring through it. Stage 3 is a medium close-up of Han Igyeom with Cheon Bongsu leaning in. Dusty shafts of light.

[Audio]
<a long horn blast outside>, <distant galloping hooves>, <swords half-drawn>. Jo Yun speaks Korean in a smooth, soft, measured tenor, calm and courteous. A soldier shouts from outside in a young male voice. Cheon Bongsu whispers in a loud, gruff, earnest voice of a stocky man in his forties. Han Igyeom mutters in a deep young male voice with the tired tone of a middle-aged office worker.

[Maintain Consistency]
Keep all three faces and clothing identical to their references; keep the counted sacks and the empty wall behind them.
```

## 클립 08A — 거실, 아침 (20초)

**참조**: 1 박만수 시트, 2 정숙 시트, 3 거실

```
[Generation Goal]
A comic wake-up: a middle-aged man wakes on his sofa still muttering a number from his dream, and his wife cuts him off.

[Reference Material Roles]
@Image 1 defines Park Mansu's face, hairstyle, build and clothing. Do not use the grey background or the panel layout.
@Image 2 defines Jeongsuk's face, hairstyle, build and clothing. Do not use the grey background or the panel layout.
@Image 3 defines the apartment living room, sofa and dining area. @Image 3 is a style reference only, not a fixed keyframe.

[Subjects and Relationships]
Park Mansu lies on the sofa clutching the TV remote in both hands like a sword hilt. Jeongsuk stands in the dining area behind the sofa, holding a rice paddle. The top of Jeongsuk's head reaches Park Mansu's nose when he stands.

[Event Script]
Stage 1 - Waking: A phone alarm rings. Park Mansu opens his eyes. Jeongsuk calls out in Korean, {여보, 출근 안 해?} Park Mansu looks at his wrinkled hands, then pats his round belly. He mumbles in Korean, {백이십 석.} End state: he stares at the ceiling.
Stage 2 - Reality: Jeongsuk says in Korean, {백이십 석 같은 소리 하고 있네. 일곱 시 반이야!} Park Mansu sits up and groans in Korean, {아이고.} He grabs his lower back; this time it really hurts. End state: hold on him wincing with a hand on his back.

[Visual and Camera Treatment]
Stage 1 is a medium shot over the sofa with Jeongsuk in soft focus behind, then a close-up of his hands. Stage 2 is a two-shot. Bright morning daylight from the balcony window.

[Audio]
<phone alarm>, <rice cooker steam>. Park Mansu speaks Korean in a warm, slightly husky baritone of a man in his fifties, groggy. Jeongsuk speaks Korean in a bright, brisk, warm voice of a woman in her forties.

[Maintain Consistency]
Keep both faces and clothing identical to their references. The way Park Mansu grabs his lower back mirrors Han Igyeom's waking gesture.
```

## 클립 08B — 현관 (15초)

**참조**: 1 박만수 경비복 시트, 2 하은 시트, 3 현관

```
[Generation Goal]
A quiet ending beat: the father leaves for his new night-guard job, and his daughter notices something odd on his phone.

[Reference Material Roles]
@Image 1 defines Park Mansu's face, hairstyle, build and security-guard uniform. Do not use the grey background or the panel layout.
@Image 2 defines Haeun's face, hairstyle, build and clothing. Do not use the grey background or the panel layout.
@Image 3 defines the apartment entrance hall with the shoe rack and front door. @Image 3 is a style reference only, not a fixed keyframe.

[Subjects and Relationships]
Park Mansu stands at the front door buttoning his guard uniform with one hand and typing on his phone with the other. Haeun comes out of her room behind him and stops at his shoulder.

[Event Script]
Stage 1 - The search: Park Mansu types on his phone. An insert shows the screen with a Korean search query: 쌀 한 섬 몇 킬로. Haeun glances at the screen and asks in Korean, {아빠, 그걸 왜 찾아?} End state: he lowers the phone.
Stage 2 - Leaving: Park Mansu puts the phone in his pocket and says simply in Korean, {팔백 명을 먹여야 돼서.} He opens the door and goes out. The door closes. End state: hold on Haeun looking at the closed door.

[Visual and Camera Treatment]
Stage 1 is a medium two-shot from the side with an insert of the phone screen. Stage 2 ends on a close-up of Haeun. Soft morning light from a small window.

[Audio]
<keys jingling>, <door closing>. Park Mansu speaks Korean in a warm, slightly husky baritone of a man in his fifties, speaking slowly and politely. Haeun speaks Korean in a low, flat, tired voice of a woman in her late twenties.

[Maintain Consistency]
Keep both faces and clothing identical to their references.
```

---

## 참조 이미지 ID (힉스필드 job)

| 이름 | 파일 | job |
|---|---|---|
| 한이겸 시트 | `docs/sheets/hanigyeom.png` | `63cb6e08-d28c-4664-af11-533a329286cb` |
| 천봉수 시트 | `docs/sheets/cheonbongsu.png` | `52fad13a-8e00-49bf-881b-0bdaa5e32315` |
| 조윤 시트 | `docs/sheets/joyun.png` | `24c87eb6-9680-424b-bfc6-a206ecaf1c76` |
| 박만수 시트 | `docs/sheets/parkmansu.png` | `98e0a6a0-cb83-4572-8339-67c05035e377` |
| 정숙 시트 | `docs/sheets/jeongsuk.png` | `b843e5a5-b920-4b9a-b473-9515449371f1` |
| 하은 시트 | `docs/sheets/haeun.png` | `4260d24f-e8ae-43d9-8bbe-cfb1ea3341c9` |
| 최 상무 시트 | `docs/sheets/choi.png` | `059450e6-1190-4951-8559-641bb0c48d51` |
| 관리소장 시트 | `docs/sheets/manager.png` | `694d2811-b832-4af3-883a-55d6ad5c4c90` |
| 군막 | `docs/locations/tent_a.png` | `d21fdb03-3a84-43d0-aa8f-7d882fabf861` |
| 성루 | `docs/locations/wall_a.png` | `d612bedc-0345-4e7e-8951-87b598c08a1f` |
| 물류센터 사무실 | `docs/locations/office.png` | `b2ac4035-849f-458d-af70-eb0376330ef5` |
| 물류센터 창고 | `docs/locations/warehouse.png` | `7d197106-d9e2-4757-9816-77bf49c2c4ea` |
| 관리사무소 | `docs/locations/mgmt_office.png` | `526d3341-2994-4e87-b84e-22120c586251` |
| 지휘 군막, 군량 창고, 거실, 현관, 박만수 경비복 | 아직 없음 | |
