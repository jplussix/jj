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
| 03 | 3 | 관리사무소 | 30초 | 박만수, 관리소장 | **생성 완료** (Claude판 채택, `renders/ep01/clip03_take1_claude.mp4`) |
| 04A | 4 | 거실 식탁, 밤 | 23초 | 박만수, 정숙, 하은 | 프롬프트 완료 (Argon, 검수) |
| 04B | 4 | 거실 소파, 밤 | 10초 | 박만수 | 프롬프트 완료 (Argon, 검수 수정 2곳) |
| 05A | 5 | 군막 | 30초 | 한이겸 | **생성 완료** |
| 05B | 5 | 군막 | 30초 | 한이겸, 천봉수 | 프롬프트 완료 |
| 06A | 6 | 성루, 아침 | 25초 | 한이겸, 천봉수, 조윤, 군관들 | 프롬프트 완료 |
| 06B | 6 | 지휘 군막 | 30초 | 한이겸, 천봉수, 조윤, 군관들 | 프롬프트 완료 |
| 06C | 6 | 지휘 군막 | 25초 | 한이겸, 천봉수, 조윤 | 프롬프트 완료 |
| 07A | 7 | 군량 창고 | 30초 | 한이겸, 천봉수, 조윤, 병사들 | 프롬프트 완료 |
| 07B | 7 | 군량 창고 | 25초 | 한이겸, 천봉수, 조윤 | 프롬프트 완료 |
| 07C | 7-2 | 군량 창고 | 25초 | 한이겸, 천봉수, 조윤, 병사들 | 프롬프트 작성 중 |
| 07D | 7-2 | 군량 창고 | 19초 | 한이겸, 천봉수, 조윤 | 프롬프트 완료 (Argon, 검수: 둘로 나눔) |
| 07D2 | 7-2 | 군량 창고 | 20초 | 한이겸, 천봉수, 조윤 | 프롬프트 완료 (Argon, 검수) |
| 07E | 7-3 | 성문 안 마당 | 25초 | 한이겸, 천봉수, 조윤, 군관들 | 프롬프트 작성 중 |
| 07F | 7-3 | 성문 안 마당 | 25초 | 한이겸, 천봉수, 조윤 | 프롬프트 작성 중 |
| 07G | 7-4 | 성문 안 마당 | 25초 | 한이겸, 김종서, 천봉수, 조윤, 군관들 | 프롬프트 작성 중 |
| 07H | 7-4 | 성문 안 마당 | 20초 | 한이겸, 김종서 | 프롬프트 작성 중 |
| 08A | 8 | 거실, 아침 | 20초 | 박만수, 정숙 | 프롬프트 완료 |
| 08B | 8 | 현관 | 15초 | 박만수(경비복), 하은 | 프롬프트 완료 |

합계 약 9분, 20클립 (07C~07H는 씬 7-2~7-4 추가분).

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

## 클립 04A — 거실 식탁, 밤 (23초)

**참조**: 1 박만수 시트, 2 정숙 시트, 3 하은 시트, 4 거실

```
[Generation Goal]
Live-action Korean family drama, real-time natural speed: at an apartment dining table at night, a laid-off father in his fifties tries and fails to tell his wife and daughter that he lost his job over dinner, then swallows the truth with a spoonful of stew and a reassuring smile. The camera stays at seated eye level.

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
At the dining table, Park Mansu always sits at the head of the table holding a metal spoon in his right hand; Jeongsuk always sits on his left side with an open household ledger and paper receipts on the tabletop in front of her; Haeun always sits on his right side holding a smartphone in her left hand with her rice bowl in front of her until she walks out of the frame to the right. A bubbling earthenware pot of doenjang stew always sits in the center of the dining table between them.

[Event Script]
0-3s: Medium two-shot at seated eye level across the corner of the dining table, framing Park Mansu at the head of the table and Jeongsuk on his left with the bubbling pot of doenjang stew in the foreground. Jeongsuk presses a paper receipt into her open household ledger while Park Mansu holds his metal spoon and shifts his gaze from Jeongsuk toward Haeun's side on his right. Both mouths closed.
3-5s: Medium close-up of Park Mansu at the head of the table, metal spoon held in his right hand. He leans forward a little. At 3s he says in Seoul-accented Korean, in a hesitant, low tone: {저기, 내가 할 말이.}
5-9s: Medium close-up of Jeongsuk at the left side of the table, with the open household ledger and paper receipts filling the foreground on the tabletop under her hands. Keeping her eyes down on the ledger, she smooths a receipt onto the page. At 5s she says in Seoul-accented Korean, in a brisk, worried tone: {여보, 이번 달 대출 이자 또 올랐어.}
9-12s: Medium close-up of Park Mansu. Hearing her words, he presses his lips together with his spoon held still above the table, then turns his head toward Haeun on his right. At 10s he says in Seoul-accented Korean, in a careful, warm tone: {하은아, 면접은.}
12-15s: Medium close-up of Haeun at the right side of the table, her rice bowl on the tabletop and her smartphone held up in front of her chest as she looks at the phone screen. At 12s she says in Seoul-accented Korean, in a flat, indifferent tone: {아빠는 몰라도 돼.}
15-17s: Medium two-shot from the front corner of the dining table showing Haeun on the right and Park Mansu at the head. Haeun rises from her chair carrying her rice bowl and smartphone and walks out of the frame to the right; a moment later only the off-screen sound of a bedroom door clicking shut is heard. Park Mansu looks at her empty chair. Both mouths closed.
17-19s: Medium close-up of Jeongsuk with the open household ledger in front of her. She lifts her eyes from the ledger toward Park Mansu. At 17s she says in Seoul-accented Korean, in a warm, casual tone: {회사는 별일 없지?}
19-23s: The key moment. Starting from a medium close-up of Park Mansu with the bubbling pot of doenjang stew clearly visible in the foreground on the table, the camera dollies in across this whole range to a tight close-up of his face. He dips his metal spoon into the pot of doenjang stew, lifts a full spoonful, and forms a faint, reassuring smile toward Jeongsuk. At 20s he says in Seoul-accented Korean, in a calm, even tone: {별일 없지.} Final frame: Park Mansu held still in the tight close-up with his spoonful of stew raised above the pot and a faint, reassuring smile on his face.

[Visual and Camera Treatment]
All shots at seated eye level, staying on the front side of the dining table along a single action line. Camera on a tripod and locked off in every shot except the dolly-in at 19-23s. Faces fill a large part of the frame in every shot, starting from a medium two-shot and moving into medium close-ups and close-ups. Lighting for this location: warm overhead pendant light illuminates the dining table and faces during dinner, while the living room sofa area is lit by the flickering blue glow of the television screen against soft warm apartment wall light.

[Audio]
No BGM; only ambient and action sounds: <soft bubbling of doenjang stew>, <paper receipt rustling against the ledger>, <metal spoon clinking against the bowl>, <wooden chair scraping softly>, <bedroom door clicking shut>. Park Mansu speaks Korean in a warm, slightly husky baritone of a man in his fifties, speaking slowly and politely. Jeongsuk speaks Korean in a bright, brisk, warm voice of a woman in her forties. Haeun speaks Korean in a low, flat, tired voice of a woman in her late twenties. Only the person speaking in each shot moves their mouth; everyone else keeps their mouth closed.

[Maintain Consistency]
@Image 1 is Park Mansu, @Image 2 is Jeongsuk, @Image 3 is Haeun, @Image 4 is the apartment living room and dining area. Keep Park Mansu's, Jeongsuk's, and Haeun's faces, hair and clothing identical to their references, including Park Mansu's charcoal grey work jacket and cheap silver wristwatch, Jeongsuk's navy floral apron and pearl stud earrings, and Haeun's oversized heather grey hoodie. Keep Park Mansu at the head of the dining table, Jeongsuk on his left with the household ledger and receipts, Haeun on his right with her smartphone and rice bowl until she walks out of frame, the pot of doenjang stew in the center of the table, and the camera on the front side of the action line. Normal human eyes. Real-time natural speed, no slow motion. No subtitles, no on-screen text.
```

## 클립 04B — 거실 소파, 밤 (10초)

**참조**: 1 박만수 시트, 2 거실

```
[Generation Goal]
Live-action Korean family drama, real-time natural speed: in an apartment living room at night, a tired father in his fifties sits on the sofa holding a remote control as a Joseon general shouts on the television screen, then droops his head and falls asleep snoring. The camera stays at seated eye level.

[Reference Material Roles]
@Image 1 defines only Park Mansu's face, hairstyle, build and clothing. Do not copy its framing, grey background or panel layout.
@Image 2 defines only the apartment living room's furniture, walls and light: the dining table with chairs, the living room sofa, the television set, and the bedroom door behind the dining area. @Image 2 is a style reference only, not a fixed keyframe.

[Subjects and Relationships]
Park Mansu corresponds to @Image 1: an original 54-year-old Korean man, broad-shouldered sturdy build with thick forearms and a slight belly, short, thick, neatly trimmed salt-and-pepper hair, grey at the temples, combed back neatly, one small dark mole on the left cheekbone just below the left eye, wearing a charcoal grey zip-up padded work jacket in matte nylon over a navy blue polo shirt with the collar visible, dark grey slacks, and a cheap silver wristwatch on the left wrist.
In the living room area, Park Mansu always sits alone on the living room sofa facing the television set, holding a black television remote control in his right hand resting on his lap, with his left forearm resting on his thigh. The television set always stands across from the sofa, its glowing screen showing a period drama scene with a bearded actor in Joseon general armor. Later that night, the dining table behind the sofa is fully cleared and bare, with the pendant lamp above it switched off, so the dining area sits in darkness.

[Event Script]
0-2s: Medium shot at seated eye level from the right side of the sofa, Park Mansu sitting alone on the sofa in the dim room, the black remote control in his right hand on his lap, blue television glow flickering across his tired face. He blinks slowly and his head bobs once as he fights off sleep. His mouth stays closed.
2-4s: Over-the-shoulder medium shot at seated eye level from beside Park Mansu on the living room sofa toward the glowing television screen, with Park Mansu's shoulder, heavy-lidded profile, and right hand gripping the black remote control on his lap clearly visible in the foreground. On the television screen, a bearded actor in Joseon general armor grips the hilt of his sword at his waist and draws the long blade free. Park Mansu's mouth stays closed.
4-7s: Same over-the-shoulder medium shot framing the glowing television screen and Park Mansu's right hand holding the black remote control in the foreground. On the television screen, the bearded actor in Joseon general armor raises the drawn long sword high above his head. At 4s the actor on the television screen shouts in Seoul-accented Korean, in a booming theatrical tone: {전군, 나를 따르라!} Park Mansu's mouth stays closed as his eyelids droop heavy with sleep.
7-10s: The key moment. Starting from a medium close-up of Park Mansu on the living room sofa with the black remote control held in his right hand on his lap, the camera dollies in across this whole range to a close-up of his sleeping face. Under the flickering blue glow from the television screen, his heavy eyelids shut completely, his chin drops onto his chest, his fingers relax around the remote control on his lap, and his lips part in a steady snore as his chest rises and falls. Final frame: Park Mansu held asleep on the sofa in a close-up with his chin resting on his chest, his mouth slightly open snoring, the black remote control in his right hand on his lap, and blue television light flickering across his face.

[Visual and Camera Treatment]
All shots at seated eye level from the right side of the sofa, with the television always to the left of Park Mansu in frame. Camera on a tripod and locked off in every shot except the dolly-in at 7-10s. Faces and the television screen fill a large part of the frame in every shot, starting from an over-the-shoulder medium shot and moving into a medium close-up and close-up. Lighting for this scene: late night, the pendant lamp over the empty dining table is off; the living room sofa area is lit only by the flickering blue glow of the television screen and one dim warm wall lamp.

[Audio]
No BGM; only ambient and action sounds: <sword-draw ring from the television speaker>, <faint fabric rustle on the sofa>, <Park Mansu's steady snoring>. The television general speaks Korean in a booming, commanding theatrical male voice. Park Mansu's voice is a warm, slightly husky baritone of a man in his fifties, speaking slowly and politely, heard here only as a steady snore in sleep. Only the person speaking in each shot moves their mouth; everyone else keeps their mouth closed.

[Maintain Consistency]
@Image 1 is Park Mansu, @Image 2 is the apartment living room. Keep Park Mansu's face, hair and clothing identical to his reference, including his charcoal grey work jacket, navy blue polo shirt, and cheap silver wristwatch on the left wrist. Keep Park Mansu seated on the living room sofa facing the television set, the black remote control in his right hand on his lap, the flickering blue television glow across his face, and the camera on the right side of the sofa. Normal human eyes. Real-time natural speed, no slow motion. No subtitles, no on-screen text.
```

---

## 클립 05B — 군막 (30초)

**참조**: 1 한이겸 시트, 2 천봉수 시트, 3 군막

```
[Generation Goal]
Live-action Korean historical comedy drama, real-time natural speed: inside a Joseon commander's tent at dawn, a young general with a middle-aged office worker's mind speaks to his loyal officer in polite modern Korean, gets his forehead checked for a fever, and puts his iron helmet on backwards before the officer turns it around. The camera stays at eye level.

[Reference Material Roles]
@Image 1 defines only Han Igyeom's face, hairstyle, build and clothing. Do not copy its framing, grey background or panel layout.
@Image 2 defines only Cheon Bongsu's face, hairstyle, build and clothing. Do not copy its framing, grey background or panel layout.
@Image 3 defines only the commander's tent's furniture, walls and light: the canvas tent walls, the wooden support pillars, the low wooden sleeping platform, the brass washbasin on its wooden stand, the burning oil lamp on the left, and the tent entrance flap on the right. @Image 3 is a style reference only, not a fixed keyframe.

[Subjects and Relationships]
Han Igyeom corresponds to @Image 1: an original 28-year-old Korean man, 185 cm, broad-shouldered powerful warrior build with a thick chest and heavy muscular arms, short full black beard and mustache, neatly trimmed, a thin pale scar cuts vertically through the outer end of the left eyebrow, long black hair tied up in a traditional Joseon topknot, with a few loose strands falling beside the face, wearing a black heavy cotton cheollik military robe with a dark crimson inner lining showing at the collar, a dark brown leather lamellar vest with small iron studs over it, a wide black leather belt with a plain brass buckle, dark trousers tucked into black leather boots, and brown leather bracers on both forearms.
Cheon Bongsu corresponds to @Image 2: an original 45-year-old Korean man, 168 cm, short and stocky with a barrel chest, thick neck and strong short arms, round broad face with full ruddy sunburnt cheeks, a short dense black mustache and a sparse short goatee, short black hair tied in a small topknot, with a black woven horsehair headband (manggeon) across the forehead, wearing brown leather lamellar armor laced with dark cord over a dark grey cotton robe, a wide brown leather belt, dark grey trousers wrapped at the shins with off-white cloth leg bindings, and worn brown leather boots.
The top of Cheon Bongsu's head reaches only Han Igyeom's nose.
Inside the commander's tent, Han Igyeom always sits upright on the edge of the raised wooden sleeping platform on the left side of the frame in his black cheollik robe, facing right toward the tent entrance, with the brass washbasin on its low wooden stand on the floor directly in front of his knees. Cheon Bongsu always stands on the tent floor on the right side of the frame inside the tent entrance flap, facing left and looking up at Han Igyeom, cradling a conical Joseon iron helmet with a rear neck-guard flap under his left arm until he hands it over.

[Event Script]
0-2s: Medium two-shot at eye level inside the tent, framing Han Igyeom seated on the edge of the wooden sleeping platform on the left, leaning over the brass washbasin on its low stand in front of him and Cheon Bongsu at the tent entrance on the right. Cheon Bongsu pushes aside the canvas tent flap with his right hand and steps inside, cradling the iron helmet under his left arm as he looks up toward Han Igyeom. Both mouths closed.
2-4s: Medium close-up of Cheon Bongsu standing inside the tent flap with the iron helmet under his left arm, looking up toward Han Igyeom. He inclines his head in a brief greeting. At 2s he says in Seoul-accented Korean, in a brisk, respectful tone: {장군, 기침하셨습니까.}
4-7s: Medium close-up of Han Igyeom seated on the edge of the sleeping platform in his black cheollik. Startled by Cheon Bongsu's greeting, he pushes the brass washbasin on its stand behind his legs and straightens up with an awkward polite smile. At 5s he says in Seoul-accented Korean, in a hesitant, polite tone: {저, 실례지만 어디서 오셨어요?}
7-10s: Medium close-up of Cheon Bongsu holding the iron helmet under his left arm. Hearing the polite speech, he freezes stiff in place with his round eyes wide open. At 7s he says in Seoul-accented Korean, in a bewildered, earnest tone: {장군, 어찌 소인한테 존대를 하십니까?}
10-14s: Medium close-up of Han Igyeom on the sleeping platform, hands resting on his knees. Realizing his slip, he shifts his eyes side to side and fumbles through different speech endings. At 10s he says in Seoul-accented Korean, in a flustered, stumbling tone: {아, 그러니까. 그대는, 누구시, 누구시오. 누구냐.}
14-17s: Close-up of Cheon Bongsu looking up at Han Igyeom. As Han Igyeom stumbles over each word, Cheon Bongsu's round eyes widen further before he straightens his neck. At 14s he says in Seoul-accented Korean, in an earnest, urgent tone: {군관 천봉수입니다. 십 년을 모셨습니다.}
17-21s: Medium two-shot at eye level framing Han Igyeom seated on the left and Cheon Bongsu standing close in front of him on the right. Cheon Bongsu reaches up and presses the back of his right hand flat against Han Igyeom's forehead while Han Igyeom sits still. At 18s he says in Seoul-accented Korean, in a worried, puzzled tone: {열은 없으신데, 말씀이 영 이상하십니다.}
21-24s: Medium close-up of Cheon Bongsu as the war drumbeat outside speeds up. Lowering his right hand, he holds the iron helmet out toward Han Igyeom with both hands. At 21s he says in Seoul-accented Korean, in an urgent, firm tone: {적이 진을 쳤습니다. 성루로 가셔야 합니다.}
24-27s: Medium close-up of Han Igyeom seated on the sleeping platform. He takes the iron helmet in both hands and places it straight down onto his head backwards, so the helmet's long rear neck-guard flap hangs down over his eyes and nose, covering the upper half of his face. His mouth stays closed.
27-30s: The key moment. Starting from a medium two-shot at eye level of Han Igyeom seated on the left with the backwards helmet covering his eyes and Cheon Bongsu standing on the right, the camera dollies in across this whole range to a tight medium two-shot of their faces. Keeping his mouth closed, Cheon Bongsu reaches up with both hands, grips the sides of the iron helmet on Han Igyeom's head, and rotates it halfway around so the neck-guard flap moves to the back of the neck and the open front reveals Han Igyeom's blinking eyes. Final frame: held for the last two seconds on Han Igyeom sitting with the iron helmet now facing forward on his head and Cheon Bongsu standing with his hands lowered, looking up at him with wide round eyes, both mouths closed.

[Visual and Camera Treatment]
All shots at eye level from the front side of the sleeping platform along a single action line, keeping Han Igyeom on the left and Cheon Bongsu on the right. Camera on a tripod and locked off in every shot except the dolly-in at 27-30s. Faces fill a large part of the frame in every shot, using only medium two-shots, medium close-ups, and a close-up. Lighting for this location: warm amber oil-lamp light from the left side of the tent illuminates the sleeping platform and faces, while cool blue dawn light filters in through the tent entrance flap on the right.

[Audio]
No BGM; only ambient and action sounds: <canvas tent flap rustling open>, <brass washbasin sliding on wood>, <distant war drum outside beating at a steady pace and then speeding up>, <leather armor creaking>, <iron helmet clinking as it is placed on and rotated>. Han Igyeom speaks Korean in a deep young male voice, but with the hesitant, overly polite tone of a tired middle-aged office worker. Cheon Bongsu speaks Korean in a loud, gruff, earnest voice of a stocky man in his forties. Only the man speaking in each shot moves his mouth; the other keeps his mouth closed.

[Maintain Consistency]
@Image 1 is Han Igyeom, @Image 2 is Cheon Bongsu, @Image 3 is the commander's tent interior. Keep Han Igyeom's and Cheon Bongsu's faces, hair, builds and clothing identical to their references, including Han Igyeom's topknot, neatly trimmed black beard, thin pale scar on the left eyebrow, black heavy cotton cheollik military robe and dark brown studded leather lamellar vest, and Cheon Bongsu's black woven horsehair headband (manggeon), short dense black mustache, and brown leather lamellar armor. Keep Han Igyeom seated on the wooden sleeping platform on the left, Cheon Bongsu standing shorter on the right looking up at him, the tent entrance flap on the right, the warm oil-lamp light from the left, and the camera on the front side of the action line. Normal human eyes. Real-time natural speed, no slow motion. No subtitles, no on-screen text.
```

**효과음 자리**: 25초 한이겸이 투구를 거꾸로 쓰는 순간 [효과음: 띠용]

## 클립 05B-2 — 군막, 투구 거꾸로 (8초)

**참조**: 1 한이겸 시트, 2 천봉수 시트, 3 군막, 4 투구 (`docs/closeups/helmet_ref_05b.png`, 05B take1 27초 프레임)

05B take1에서 투구를 거꾸로 쓰는 게 안 보여서, 0~24초는 take1을 쓰고 이 8초를 이어 붙인다.

```
[Generation Goal]
Live-action Korean historical comedy drama, real-time natural speed: inside a Joseon commander's tent at dawn, a young general puts his iron helmet on backwards so its leather neck-guard hangs over his face like a curtain, gropes blindly, and his stocky officer silently twists it around the right way. The camera stays at eye level.

[Reference Material Roles]
@Image 1 defines only Han Igyeom's face, hairstyle, build and clothing. Do not copy its framing, grey background or panel layout.
@Image 2 defines only Cheon Bongsu's face, hairstyle, build and clothing. Do not copy its framing, grey background or panel layout.
@Image 3 defines only the commander's tent's canvas walls, wooden pillars, weapon rack and light. @Image 3 is a style reference only, not a fixed keyframe.
@Image 4 defines only the iron helmet's design: a conical polished iron bowl with a red horsehair plume on top and a layered neck-guard that hangs from its back edge. Do not copy its framing or the people in it.

[Subjects and Relationships]
Han Igyeom corresponds to @Image 1: an original 28-year-old Korean man, 185 cm, broad-shouldered powerful warrior build, short full black beard and mustache, neatly trimmed, a thin pale scar through the outer end of the left eyebrow, long black hair tied up in a traditional Joseon topknot, wearing a black heavy cotton cheollik military robe with a dark crimson inner lining showing at the collar, a dark brown leather lamellar vest with small iron studs over it, and brown leather bracers on both forearms.
Cheon Bongsu corresponds to @Image 2: an original 45-year-old Korean man, 168 cm, short and stocky with a barrel chest, round broad face with full ruddy cheeks, a short dense black mustache, a black woven horsehair headband (manggeon) across the forehead, wearing brown leather lamellar armor laced with dark cord over a dark grey cotton robe.
The top of Cheon Bongsu's head reaches only Han Igyeom's nose. Han Igyeom always sits on the edge of the low wooden sleeping platform on the left of the frame; Cheon Bongsu always stands on the right, facing him.

[Event Script]
0-2s: Medium shot at eye level of Han Igyeom seated on the left, holding the iron helmet from @Image 4 in both hands in front of his chest, with the hanging neck-guard turned toward his own face. Cheon Bongsu stands on the right, hands lowered. Both mouths closed.
2-4s: Medium close-up of Han Igyeom. He jams the helmet down onto his head backwards: the layered neck-guard drops in front of his face like a curtain, covering his eyes, nose and mouth completely, and the red horsehair plume flops forward over the front. Only his beard tip shows below the neck-guard.
4-6s: Medium two-shot at eye level. Han Igyeom, blinded behind the neck-guard, sways his head and gropes the air in front of him with both hands. Cheon Bongsu stands frozen on the right, round eyes wide, mustache twitching, mouth closed.
6-8s: The key moment, same two-shot, camera locked off. Cheon Bongsu steps in, grips both sides of the helmet with his hands, and twists it a half turn so the neck-guard swings around to the back of Han Igyeom's neck and his face appears, blinking. Final frame: held still on Han Igyeom with the helmet now on correctly and blinking at Cheon Bongsu, and Cheon Bongsu with his hands lowered, staring up at him, both mouths closed.

[Visual and Camera Treatment]
All shots at eye level from the front of the sleeping platform, Han Igyeom on the left and Cheon Bongsu on the right. Camera on a tripod, locked off. Faces and the helmet fill a large part of the frame. Lighting for this location: warm amber oil-lamp light from the left side of the tent, cool blue dawn light through the entrance flap on the right.

[Audio]
No BGM; only ambient and action sounds: <iron helmet clanking down onto his head>, <muffled grunt from behind the neck-guard>, <leather armor creaking>, <iron scraping as the helmet is twisted around>, <distant fast war drums outside>. No dialogue in this clip; both mouths stay closed.

[Maintain Consistency]
@Image 1 is Han Igyeom, @Image 2 is Cheon Bongsu, @Image 3 is the tent, @Image 4 is the helmet. Keep both faces, hair and clothing identical to their references, the helmet design identical to @Image 4, Han Igyeom on the left seated and Cheon Bongsu on the right standing shorter. Normal human eyes. Real-time natural speed, no slow motion. No subtitles, no on-screen text.
```

---

## 클립 06A — 성루, 아침 (24초)

**참조**: 1 한이겸 시트, 2 천봉수 시트, 3 조윤 시트, 4 성루 아침 (`docs/locations/wall_morning.png`, media `68547fb2-…`), 5 투구 (media `5677efe3-…`) (`docs/closeups/helmet_ref_05b.png`)

```
[Generation Goal]
Live-action Korean historical comedy drama, real-time natural speed: on a Joseon fortress wall walkway in the cold morning light, a young general inhabited by a middle-aged warehouse manager looks out at the enemy camp and shocks his officers by proposing "a meeting" in polite modern Korean. The camera stays at eye level.

[Reference Material Roles]
@Image 1 defines only Han Igyeom's face, hairstyle, build and clothing. Do not copy its framing, grey background or panel layout.
@Image 2 defines only Cheon Bongsu's face, hairstyle, build and clothing. Do not copy its framing, grey background or panel layout.
@Image 3 defines only Jo Yun's face, hairstyle, build and clothing. Do not copy its framing, grey background or panel layout.
@Image 4 defines only the fortress wall's frosted stone crenellations, snowy walkway, red banners, gate tower and the morning view of the enemy tents across the snowy plain. @Image 4 is a style reference only, not a fixed keyframe.
@Image 5 defines only the design of Han Igyeom's helmet: a conical polished iron helmet with a red horsehair plume and a layered neck-guard at the back. Do not copy the people or framing in it.

[Subjects and Relationships]
Han Igyeom corresponds to @Image 1: an original 28-year-old Korean man, 185 cm, broad-shouldered powerful warrior build with a thick chest and heavy muscular arms, short full black beard and mustache, neatly trimmed, a thin pale scar cuts vertically through the outer end of the left eyebrow, long black hair tied up in a traditional Joseon topknot, with a few loose strands falling beside the face, wearing a black heavy cotton cheollik military robe with a dark crimson inner lining showing at the collar, a dark brown leather lamellar vest with small iron studs over it, a wide black leather belt with a plain brass buckle, dark trousers tucked into black leather boots, and brown leather bracers on both forearms.
Cheon Bongsu corresponds to @Image 2: an original 45-year-old Korean man, 168 cm, short and stocky with a barrel chest, thick neck and strong short arms, round broad face with full ruddy sunburnt cheeks, a short dense black mustache and a sparse short goatee, short black hair tied in a small topknot, with a black woven horsehair headband (manggeon) across the forehead, wearing brown leather lamellar armor laced with dark cord over a dark grey cotton robe, a wide brown leather belt, dark grey trousers wrapped at the shins with off-white cloth leg bindings, and worn brown leather boots.
Jo Yun corresponds to @Image 3: an original 35-year-old Korean man, 176 cm, slender with an upright, composed posture, long narrow face with pale even skin and a few faint freckles across the bridge of the nose, narrow single-lidded dark eyes with a calm, unreadable gaze, thin lips set in a faint polite half-smile, a very thin, neatly trimmed mustache, black hair tied in a tidy topknot, wearing a pale grey-blue silk dopo scholar's robe with wide sleeves, a dark navy cord sash tied high at the chest, a white inner jacket collar visible at the neck, white beoseon socks, black taesahye shoes, and a small black lacquered brush case hanging from the sash at the left hip.
The top of Cheon Bongsu's head reaches only Han Igyeom's nose.
The top of Jo Yun's head reaches Han Igyeom's eyebrows.
The top of Cheon Bongsu's head reaches Jo Yun's eyes.
Han Igyeom wears his armor and helmet as described below throughout this clip. Over his robe he now wears the full dark iron-and-leather lamellar armor coat he wore on the wall the night before, and on his head the conical polished iron helmet with a red horsehair plume and a layered neck-guard at the back, worn correctly with his face fully visible. Han Igyeom always stands on the left side of the frame against the stone crenellations, facing right toward his officers with the snowy plain and enemy tents behind his shoulder. Cheon Bongsu always stands in the center-right foreground facing Han Igyeom and tilting his head up to look at him, flanked by minor officers in brown leather armor whose faces stay in partial profile. Jo Yun always stands one step behind Cheon Bongsu on the far right, upright with both hands tucked inside his wide grey-blue silk sleeves.

[Event Script]
0-2s: Medium shot at eye level on the fortress walkway framing Han Igyeom on the left at the stone crenellations, Cheon Bongsu in the center looking up at him, and Jo Yun one step behind on the right with hands tucked in his sleeves. Han Igyeom grips the frost-covered stone merlon with both hands and shifts his gaze from the enemy tents on the plain back to his officers. All mouths closed.
2-7s: Medium close-up of Cheon Bongsu at eye level, head tilted back as he looks up toward Han Igyeom with wide, earnest eyes. At 2s he says in Seoul-accented Korean, in an urgent, commanding tone, pronouncing "장군" clearly as "jang-goon", with a distinct final n: {적이 육천입니다. 아군은 팔백입니다. 장군, 명을 내리소서.}
7-11s: The key moment. Starting from a medium close-up of Han Igyeom at the stone crenellations, the camera dollies in across this whole range to a close-up of his face. He releases the stone merlon, brings both open palms together in front of his chest like an office manager calling a morning huddle, and looks around at the officers. At 8s he says in Seoul-accented Korean, in a polite, matter-of-fact office tone: {일단 회의부터 합시다.}
11-15s: Medium two-shot of Cheon Bongsu in the foreground and Jo Yun standing behind his shoulder, camera locked off. Two minor officers at the edge exchange bewildered glances while Cheon Bongsu blinks his round eyes in disbelief and leans his head forward. At 11s Cheon Bongsu says in Seoul-accented Korean, in a baffled, flustered tone, pronouncing "장군" clearly as "jang-goon", with a distinct final n: {장군, 저희한테 '합시다'라니요.}
15-18s: Medium close-up of Cheon Bongsu, brows furrowed deep over his round ruddy face as he tilts his head slightly. At 15s he says in Seoul-accented Korean, in an earnest, puzzled tone: {그리고 회의가 무엇입니까?}
18-22s: Medium close-up of Han Igyeom at the crenellations, camera locked off. He gestures toward an imaginary table with both hands, then winces and shifts his eyes side to side as he fumbles his speech ending from polite modern Korean to blunt command speech. At 18s he says in Seoul-accented Korean, in a flustered, stumbling tone: {다 같이 앉아서 얘기하는 거예요. 아니, …것이오. 것이다!}
22-24s: Medium close-up of Jo Yun standing one step behind Cheon Bongsu's shoulder with both hands tucked inside his wide grey-blue sleeves. His faint polite half-smile stays fixed while his narrow single-lidded eyes narrow slightly as he studies Han Igyeom. Final frame: held for the last two seconds on Jo Yun's still, watchful face and Cheon Bongsu's perplexed profile in the foreground, all mouths closed.

[Visual and Camera Treatment]
All shots at standing eye level from the inner side of the fortress walkway, keeping Han Igyeom on the left and Cheon Bongsu and Jo Yun on the right of the action line. Camera on a tripod and locked off in every shot except the dolly-in at 7-11s. Faces fill a large part of the frame in every shot, using only medium shots, medium two-shots, and medium close-ups. Lighting for this location: crisp, cold morning sunlight from the left illuminates the stone battlements and faces, with bright snow glare rising from the plain beyond the wall.

[Audio]
No BGM; only ambient and action sounds: <cold northern wind whistling across stone battlements>, <leather armor creaking>, <distant low horn from the enemy camp across the plain>. Han Igyeom speaks Korean in a deep young male voice, but with the hesitant, overly polite tone of a tired middle-aged office worker. Cheon Bongsu speaks Korean in a loud, gruff, earnest voice of a stocky man in his forties. Jo Yun (a smooth, soft, measured tenor, calm and courteous) remains silent with his mouth closed throughout this clip. Only the man speaking in each shot moves his mouth; the others keep their mouths closed.

[Maintain Consistency]
@Image 1 is Han Igyeom, @Image 2 is Cheon Bongsu, @Image 3 is Jo Yun, @Image 4 is the fortress wall walkway. @Image 5 shows only the design of Han Igyeom's helmet; do not copy the people or framing in it. Keep all three men's faces, hairstyles, builds and clothing identical to their references, including Han Igyeom's topknot, neatly trimmed black beard, thin pale scar on the left eyebrow, black cheollik robe under the full lamellar armor coat and the red-plumed iron helmet, Cheon Bongsu's black horsehair headband (manggeon), short dense black mustache and brown leather lamellar armor, and Jo Yun's pale grey-blue silk dopo robe, dark navy chest sash and small black lacquered brush case at the left hip. Keep Han Igyeom on the left at the crenellations, Cheon Bongsu shorter in the center looking up at him, Jo Yun one step behind on the right with hands in his sleeves, and the camera on the walkway side of the action line. Normal human eyes. Real-time natural speed, no slow motion. No subtitles, no on-screen text.
```

**효과음 자리**: 10초 "일단 회의부터 합시다" 직후 [효과음: 정적]

## 클립 06B — 지휘 군막, 회의 (24초)

**참조**: 1 한이겸 시트, 2 천봉수 시트, 3 조윤 시트, 4 지휘 군막

```
[Generation Goal]
Live-action Korean historical comedy drama, real-time natural speed: inside a Joseon command tent, stiffly seated military officers whisper about their general falling off his horse, snap upright when caught, and watch as the general asks the composed secretary for the grain ledger. The camera stays at seated eye level.

[Reference Material Roles]
@Image 1 defines only Han Igyeom's face, hairstyle, build and clothing. Do not copy its framing, grey background or panel layout.
@Image 2 defines only Cheon Bongsu's face, hairstyle, build and clothing. Do not copy its framing, grey background or panel layout.
@Image 3 defines only Jo Yun's face, hairstyle, build and clothing. Do not copy its framing, grey background or panel layout.
@Image 4 defines only the command tent's furniture, walls and light: the canvas tent walls, the wooden support pillars, the long low wooden conference table in the center, the floor cushions, and the hanging brass oil lanterns. @Image 4 is a style reference only, not a fixed keyframe.

[Subjects and Relationships]
Han Igyeom corresponds to @Image 1: an original 28-year-old Korean man, 185 cm, broad-shouldered powerful warrior build with a thick chest and heavy muscular arms, short full black beard and mustache, neatly trimmed, a thin pale scar cuts vertically through the outer end of the left eyebrow, long black hair tied up in a traditional Joseon topknot, with a few loose strands falling beside the face, wearing a black heavy cotton cheollik military robe with a dark crimson inner lining showing at the collar, a dark brown leather lamellar vest with small iron studs over it, a wide black leather belt with a plain brass buckle, dark trousers tucked into black leather boots, and brown leather bracers on both forearms.
Cheon Bongsu corresponds to @Image 2: an original 45-year-old Korean man, 168 cm, short and stocky with a barrel chest, thick neck and strong short arms, round broad face with full ruddy sunburnt cheeks, a short dense black mustache and a sparse short goatee, short black hair tied in a small topknot, with a black woven horsehair headband (manggeon) across the forehead, wearing brown leather lamellar armor laced with dark cord over a dark grey cotton robe, a wide brown leather belt, dark grey trousers wrapped at the shins with off-white cloth leg bindings, and worn brown leather boots.
Jo Yun corresponds to @Image 3: an original 35-year-old Korean man, 176 cm, slender with an upright, composed posture, long narrow face with pale even skin and a few faint freckles across the bridge of the nose, narrow single-lidded dark eyes with a calm, unreadable gaze, thin lips set in a faint polite half-smile, a very thin, neatly trimmed mustache, black hair tied in a tidy topknot, wearing a pale grey-blue silk dopo scholar's robe with wide sleeves, a dark navy cord sash tied high at the chest, a white inner jacket collar visible at the neck, white beoseon socks, black taesahye shoes, and a small black lacquered brush case hanging from the sash at the left hip.
The top of Cheon Bongsu's head reaches only Han Igyeom's nose.
The top of Jo Yun's head reaches Han Igyeom's eyebrows.
The top of Cheon Bongsu's head reaches Jo Yun's eyes.
Han Igyeom keeps the full dark lamellar armor coat on over his black cheollik, with his red-plumed iron helmet taken off and resting on the table beside his right hand; his topknot and face are fully visible. Han Igyeom always sits on a floor cushion at the head of the long low wooden table on the left side of the frame, facing right down the table. Cheon Bongsu always sits at the near side of the table to Han Igyeom's right with his back unnaturally straight and both hands flat on his knees. Jo Yun always sits across the table to Han Igyeom's left on the center-right of the frame, with a thick string-bound Joseon paper ledger resting flat on the wooden tabletop under his right hand. Two minor officers in brown leather armor—Officer 1 (a thin man in his thirties) and Officer 2 (a grey-bearded man in his fifties)—always sit side by side further down the table on the far right.

[Event Script]
0-2s: Medium shot at seated eye level inside the command tent framing Han Igyeom at the head of the low wooden table on the left, Cheon Bongsu on the near side, and Jo Yun across from him with his hand on the closed paper ledger. All sit with stiff, board-straight backs and hands on their knees. All mouths closed.
2-5s: Medium two-shot at seated eye level of Officer 1 (thin, thirties) and Officer 2 (grey-bearded, fifties) seated side by side on the right side of the table, leaning their heads close together with shoulders hunched. Officer 1 cups his left hand beside his mouth and glances toward the head of the table. At 2s Officer 1 says in Seoul-accented Korean, in a hushed, gossipy whisper: {장군님 말씀이 왜 저러시나.}
5-8s: Same medium two-shot of the two whispering officers leaning close together. Officer 2 raises his eyebrows and nods knowingly toward Officer 1. At 5s Officer 2 says in Seoul-accented Korean, in a low, conspiratorial whisper: {어젯밤에 말에서 떨어지셨다던데.}
8-9s: Medium close-up of Han Igyeom at the head of the table, camera locked off. He turns his head and fixes a flat, steady stare directly toward the two whispering officers. Mouth closed.
9-11s: The key moment. Medium two-shot of Officer 1 and Officer 2, camera locked off. Catching Han Igyeom's gaze, both officers snap their backs bolt upright at the exact same instant, press their palms flat onto their knees, and stare straight ahead with rigid, blank faces, mouths closed.
11-15s: Medium close-up of Han Igyeom at the head of the wooden table, resting both forearms on the table edge like a department manager opening a status review. At 11s he says in Seoul-accented Korean, in a businesslike office tone: {먼저 현황부터. 쌀이 얼마나 남았소?}
15-19s: Medium close-up of Jo Yun seated at the table with his right hand resting on the closed string-bound paper ledger, a faint polite half-smile on his lips. At 15s he says in Seoul-accented Korean, in a smooth, assured tone: {삼백 석입니다. 넉 달은 버팁니다.}
19-22s: Medium close-up of Han Igyeom looking across the table at Jo Yun and extending his right hand palm-up onto the tabletop. At 19s he says in Seoul-accented Korean, in a calm, polite office tone: {장부 좀 봅시다.}
22-24s: Medium two-shot at seated eye level of Han Igyeom on the left and Jo Yun on the right across the low wooden table. Jo Yun's fingers pause for a beat on the cover of the string-bound ledger before he slides the closed ledger smoothly across the wooden tabletop to rest in front of Han Igyeom. Final frame: held on Han Igyeom looking down with his right hand resting on the ledger cover and Jo Yun watching him with a faint polite half-smile, both mouths closed.

[Visual and Camera Treatment]
All shots at seated eye level from the near side of the long wooden table along a single action line, keeping Han Igyeom at the head on the left and Jo Yun and the officers on the right. Camera on a tripod and locked off in every shot. Faces fill a large part of the frame in every shot, using only medium shots, medium two-shots, and medium close-ups. Lighting for this location: warm amber oil-lamp light from brass lanterns inside the command tent illuminates the wooden table and faces, while cool morning daylight filters through the canvas walls.

[Audio]
No BGM; only ambient and action sounds: <leather armor creaking as the officers sit stiffly and snap upright>, <wind buffeting the canvas tent walls>, <paper ledger sliding across the wooden tabletop>. Officer 1 speaks Korean in a hushed, nervous young male voice. Officer 2 speaks Korean in a low, hoarse older male voice. Han Igyeom speaks Korean in a deep young male voice, but with the hesitant, overly polite tone of a tired middle-aged office worker. Jo Yun speaks Korean in a smooth, soft, measured tenor, calm and courteous. Cheon Bongsu (a loud, gruff, earnest voice of a stocky man in his forties) remains silent with his mouth closed throughout this clip. Only the man speaking in each shot moves his mouth; the others keep their mouths closed.

[Maintain Consistency]
@Image 1 is Han Igyeom, @Image 2 is Cheon Bongsu, @Image 3 is Jo Yun, @Image 4 is the command tent interior. Keep all three men's faces, hairstyles, builds and clothing identical to their references, including Han Igyeom's topknot, neatly trimmed black beard, thin pale scar on the left eyebrow, black cheollik robe under the full lamellar armor coat, with the red-plumed helmet resting on the table, Cheon Bongsu's black horsehair headband (manggeon), short dense black mustache and brown leather lamellar armor, and Jo Yun's pale grey-blue silk dopo robe, dark navy chest sash and small black lacquered brush case at the left hip. Keep Han Igyeom seated at the head of the table on the left, Cheon Bongsu on the near side, Jo Yun across from him on the right, and the camera on the near side of the action line. Normal human eyes. Real-time natural speed, no slow motion. No subtitles, no on-screen text.
```

## 클립 06C — 지휘 군막, 장부 (28초)

**참조**: 1 한이겸 시트, 2 천봉수 시트, 3 조윤 시트, 4 지휘 군막

```
[Generation Goal]
Live-action Korean historical comedy drama, real-time natural speed: inside the Joseon command tent, the general audits the grain ledger with a warehouse manager's sharp eye, points out that three months of receiving signatures are in the same handwriting, and orders an immediate physical count at the storehouse. The camera stays at eye level.

[Reference Material Roles]
@Image 1 defines only Han Igyeom's face, hairstyle, build and clothing. Do not copy its framing, grey background or panel layout.
@Image 2 defines only Cheon Bongsu's face, hairstyle, build and clothing. Do not copy its framing, grey background or panel layout.
@Image 3 defines only Jo Yun's face, hairstyle, build and clothing. Do not copy its framing, grey background or panel layout.
@Image 4 defines only the command tent's furniture, walls and light: the canvas tent walls, the wooden support pillars, the long low wooden conference table, the floor cushions, and the hanging brass oil lanterns. @Image 4 is a style reference only, not a fixed keyframe.

[Subjects and Relationships]
Han Igyeom corresponds to @Image 1: an original 28-year-old Korean man, 185 cm, broad-shouldered powerful warrior build with a thick chest and heavy muscular arms, short full black beard and mustache, neatly trimmed, a thin pale scar cuts vertically through the outer end of the left eyebrow, long black hair tied up in a traditional Joseon topknot, with a few loose strands falling beside the face, wearing a black heavy cotton cheollik military robe with a dark crimson inner lining showing at the collar, a dark brown leather lamellar vest with small iron studs over it, a wide black leather belt with a plain brass buckle, dark trousers tucked into black leather boots, and brown leather bracers on both forearms.
Cheon Bongsu corresponds to @Image 2: an original 45-year-old Korean man, 168 cm, short and stocky with a barrel chest, thick neck and strong short arms, round broad face with full ruddy sunburnt cheeks, a short dense black mustache and a sparse short goatee, short black hair tied in a small topknot, with a black woven horsehair headband (manggeon) across the forehead, wearing brown leather lamellar armor laced with dark cord over a dark grey cotton robe, a wide brown leather belt, dark grey trousers wrapped at the shins with off-white cloth leg bindings, and worn brown leather boots.
Jo Yun corresponds to @Image 3: an original 35-year-old Korean man, 176 cm, slender with an upright, composed posture, long narrow face with pale even skin and a few faint freckles across the bridge of the nose, narrow single-lidded dark eyes with a calm, unreadable gaze, thin lips set in a faint polite half-smile, a very thin, neatly trimmed mustache, black hair tied in a tidy topknot, wearing a pale grey-blue silk dopo scholar's robe with wide sleeves, a dark navy cord sash tied high at the chest, a white inner jacket collar visible at the neck, white beoseon socks, black taesahye shoes, and a small black lacquered brush case hanging from the sash at the left hip.
The top of Cheon Bongsu's head reaches only Han Igyeom's nose.
The top of Jo Yun's head reaches Han Igyeom's eyebrows.
The top of Cheon Bongsu's head reaches Jo Yun's eyes.
Han Igyeom wears the full dark lamellar armor coat over his black cheollik, helmet off, topknot visible. Han Igyeom always occupies the left side of the frame at the head of the low wooden table, with the open string-bound paper ledger lying flat on the tabletop in front of him until he stands at 18s. Cheon Bongsu always sits on the near side of the table in the center-right foreground and stands beside the table when Han Igyeom rises, looking up at him. Jo Yun always sits across the table on the right side of the frame, with his wide grey-blue silk sleeves resting on the table edge.

[Event Script]
0-2s: Medium close-up at seated eye level of Han Igyeom at the head of the wooden table, looking down at the open paper ledger lying flat in front of him. He turns one paper page with his left hand and traces his right index finger down a vertical column of brush-written entries, stopping his fingertip on a specific line. Mouth closed.
2-7s: Medium close-up of Han Igyeom keeping his right index finger pressed on that line of the ledger while looking at the page. At 2s he says in Seoul-accented Korean, in a focused, analytical office tone: {지난달에 이백 석이 들어왔는데, 나간 건 오십 석이네.}
7-9s: Medium close-up of Jo Yun seated across the table, hands resting inside his wide sleeves on the table edge, nodding slightly. At 7s he says in Seoul-accented Korean, in a calm, courteous tone: {그렇습니다.}
9-14s: Medium two-shot at seated eye level of Han Igyeom on the left with his finger on the open ledger and Jo Yun on the right across the table. Jo Yun's shoulders drop slightly in visible relief as Han Igyeom nods at the numbers. At 9s Han Igyeom says in Seoul-accented Korean, in a steady, matter-of-fact tone: {그 전에 남은 게 백오십 석. 합치면 삼백 석. 숫자는 맞소.}
14-18s: The key moment. Starting from a medium two-shot of Han Igyeom tapping three consecutive signature marks at the bottom of the ledger page with his index finger and Jo Yun seated on the right, the camera dollies in across this whole range toward Jo Yun's face and sleeve resting on the table edge. As Han Igyeom speaks, Jo Yun's faint half-smile stiffens; at the cuff of his wide grey-blue silk sleeve resting on the table, his visible knuckles slowly clench into a tight fist, the silk bunching around it. At 14s Han Igyeom says in Seoul-accented Korean, in a sharp, pointed tone: {그런데 받은 사람 수결이 석 달째 한 사람 글씨요.}
18-23s: Medium two-shot at eye level. Han Igyeom rises to his full height at the head of the table on the left, leaving the ledger open on the table; Cheon Bongsu, already standing on the right, tilts his head back to look up at him. At 18s Han Igyeom says in Seoul-accented Korean, in a firm warehouse-supervisor tone: {입고하는 사람하고 확인하는 사람이 같으면 안 되지. 창고 갑시다.}
23-26s: Medium close-up of Cheon Bongsu standing on the right and looking sharply upward toward Han Igyeom with wide round eyes. At 23s he says in Seoul-accented Korean, in a startled, urgent tone: {지금 말입니까? 적이 코앞인데.}
26-28s: Medium two-shot at standing eye level of Han Igyeom towering on the left and Cheon Bongsu looking up at him on the right. At 26s Han Igyeom says in Seoul-accented Korean, in an unshakeable, practical tone: {그러니까 지금 세야지.} Final frame: held on Han Igyeom standing tall with a resolute gaze and Cheon Bongsu staring up at him with round eyes, both mouths closed.

[Visual and Camera Treatment]
All shots at eye level (seated eye level from 0-18s, standing eye level from 18-28s) from the near side of the wooden table along a single action line, keeping Han Igyeom on the left and Cheon Bongsu and Jo Yun on the right. Camera on a tripod and locked off in every shot except the dolly-in at 14-18s. Faces fill a large part of the frame in every shot. Lighting for this location: warm amber oil-lamp light from brass lanterns inside the command tent illuminates the wooden table and faces, while cool morning daylight filters through the canvas walls.

[Audio]
No BGM; only ambient and action sounds: <crisp paper ledger page turning>, <fingertip tapping paper>, <silk sleeve fabric tightening>, <leather armor rustling as Han Igyeom and Cheon Bongsu stand>. Han Igyeom speaks Korean in a deep young male voice, but with the hesitant, overly polite tone of a tired middle-aged office worker, growing firmer and more confident when auditing numbers. Jo Yun speaks Korean in a smooth, soft, measured tenor, calm and courteous. Cheon Bongsu speaks Korean in a loud, gruff, earnest voice of a stocky man in his forties. Only the man speaking in each shot moves his mouth; the others keep their mouths closed.

[Maintain Consistency]
@Image 1 is Han Igyeom, @Image 2 is Cheon Bongsu, @Image 3 is Jo Yun, @Image 4 is the command tent interior. Keep all three men's faces, hairstyles, builds and clothing identical to their references, including Han Igyeom's topknot, neatly trimmed black beard, thin pale scar on the left eyebrow, black cheollik robe under the full lamellar armor coat, Cheon Bongsu's black horsehair headband (manggeon), short dense black mustache and brown leather lamellar armor, and Jo Yun's pale grey-blue silk dopo robe, dark navy chest sash and small black lacquered brush case at the left hip. Keep Han Igyeom on the left, Cheon Bongsu and Jo Yun on the right, and the camera on the near side of the action line. Normal human eyes. Real-time natural speed, no slow motion. No subtitles, no on-screen text.
```

## 클립 07A — 군량 창고, 세기 (28초)

**참조**: 1 한이겸 시트, 2 천봉수 시트, 3 조윤 시트, 4 군량 창고

```
[Generation Goal]
Live-action Korean historical comedy drama, real-time natural speed: inside a wooden fortress grain storehouse, soldiers pull away the front row of straw rice sacks to expose an empty hollow space behind them, count out only twelve rows of ten, and burst into stifled laughter when the general deadpans that rats eating a hundred and eighty sacks would be the size of cows. The camera stays at eye level.

[Reference Material Roles]
@Image 1 defines only Han Igyeom's face, hairstyle, build and clothing. Do not copy its framing, grey background or panel layout.
@Image 2 defines only Cheon Bongsu's face, hairstyle, build and clothing. Do not copy its framing, grey background or panel layout.
@Image 3 defines only Jo Yun's face, hairstyle, build and clothing. Do not copy its framing, grey background or panel layout.
@Image 4 defines only the wooden grain storehouse's walls, timber pillars, plank floor, straw rice sacks, and daylight shafts. @Image 4 is a style reference only, not a fixed keyframe.

[Subjects and Relationships]
Han Igyeom corresponds to @Image 1: an original 28-year-old Korean man, 185 cm, broad-shouldered powerful warrior build with a thick chest and heavy muscular arms, short full black beard and mustache, neatly trimmed, a thin pale scar cuts vertically through the outer end of the left eyebrow, long black hair tied up in a traditional Joseon topknot, with a few loose strands falling beside the face, wearing a black heavy cotton cheollik military robe with a dark crimson inner lining showing at the collar, a dark brown leather lamellar vest with small iron studs over it, a wide black leather belt with a plain brass buckle, dark trousers tucked into black leather boots, and brown leather bracers on both forearms.
Cheon Bongsu corresponds to @Image 2: an original 45-year-old Korean man, 168 cm, short and stocky with a barrel chest, thick neck and strong short arms, round broad face with full ruddy sunburnt cheeks, a short dense black mustache and a sparse short goatee, short black hair tied in a small topknot, with a black woven horsehair headband (manggeon) across the forehead, wearing brown leather lamellar armor laced with dark cord over a dark grey cotton robe, a wide brown leather belt, dark grey trousers wrapped at the shins with off-white cloth leg bindings, and worn brown leather boots.
Jo Yun corresponds to @Image 3: an original 35-year-old Korean man, 176 cm, slender with an upright, composed posture, long narrow face with pale even skin and a few faint freckles across the bridge of the nose, narrow single-lidded dark eyes with a calm, unreadable gaze, thin lips set in a faint polite half-smile, a very thin, neatly trimmed mustache, black hair tied in a tidy topknot, wearing a pale grey-blue silk dopo scholar's robe with wide sleeves, a dark navy cord sash tied high at the chest, a white inner jacket collar visible at the neck, white beoseon socks, black taesahye shoes, and a small black lacquered brush case hanging from the sash at the left hip.
The top of Cheon Bongsu's head reaches only Han Igyeom's nose.
The top of Jo Yun's head reaches Han Igyeom's eyebrows.
The top of Cheon Bongsu's head reaches Jo Yun's eyes.
Han Igyeom wears the full dark lamellar armor coat over his black cheollik, helmet off, topknot visible. Han Igyeom always stands on the left side of the storehouse floor facing right toward the straw rice sacks. Cheon Bongsu always stands in the center beside the rows of straw sacks, holding the open paper ledger in his left hand and an inked brush in his right hand. Jo Yun always stands on the right near the storehouse doorway with his hands tucked inside his wide grey-blue sleeves. Background soldiers in plain grey cotton uniforms and cloth headbands stay behind the sacks with their faces small or in profile, except one young soldier standing behind Cheon Bongsu's shoulder at 22-28s.

[Event Script]
0-2s: Medium two-shot at eye level inside the storehouse framing Han Igyeom on the left and Cheon Bongsu in the center holding the open ledger in his left hand and an inked brush in his right, with a wall of stacked straw rice sacks behind them. Both mouths closed.
2-5s: Medium close-up of Han Igyeom at eye level. He points his right hand toward the stacked straw sacks and motions horizontally to line them up. At 2s he says in Seoul-accented Korean, in a brisk warehouse-manager tone: {한 줄에 열 섬씩. 줄 맞춰 다시 쌓으시오.}
5-9s: Medium shot at eye level of two soldiers in grey cotton uniforms pulling two straw sacks off the front layer of the stack; as the front sacks come away, a wide hollow space opens directly behind the single front row, revealing the bare wooden plank wall and bare floorboards behind it. In the foreground, Cheon Bongsu turns his head with wide round eyes while the soldiers exchange startled glances. All mouths closed.
9-13s: Hard cut, a little later: the sacks are now laid out on the floor in neat rows of ten. Medium shot at eye level of Cheon Bongsu standing beside the neat rows of straw sacks laid out on the floor, holding the open ledger in his left hand and pointing with his right index finger along the final three rows in turn. At 9s he says in Seoul-accented Korean, in an earnest, counting tone: {열, 열하나, 열둘. 열두 줄입니다.}
13-15s: Medium close-up of Han Igyeom looking down at the counted rows on the floor, his jaw set. At 13s he says in Seoul-accented Korean, in a flat, certain tone: {백이십 석.}
15-19s: Medium close-up of Cheon Bongsu holding the open ledger up at chest height in his left hand; with the inked brush in his right hand, he draws a bold black stroke across the original brush-written entry and writes the corrected count beside it, then looks up toward Jo Yun on the right. At 16s he says in Seoul-accented Korean, in a shocked, grave tone: {백여든 석이 빕니다.}
19-22s: Medium close-up of Jo Yun standing near the doorway on the right with his hands tucked inside his wide grey-blue sleeves, his face completely impassive as Cheon Bongsu and the officers look toward him. At 19s Jo Yun says in Seoul-accented Korean, in a smooth, deadpan tone: {쥐가 들었나 봅니다.}
22-26s: The key moment. Starting from a medium close-up of Han Igyeom on the left, the camera dollies in across this whole range to a close-up of his deadpan face. He holds both hands wide apart at chest width to show the bulk of a full-grown cow while staring straight at Jo Yun. At 22s he says in Seoul-accented Korean, in a dry, deadpan middle-aged office worker tone: {쥐가 백여든 석을 먹으면 소만 해졌겠소.}
26-28s: Medium two-shot at eye level of Cheon Bongsu in the foreground and a young soldier in a grey cotton uniform standing right behind his shoulder; the young soldier puffs out his cheeks bursting into a laugh and claps both hands tightly over his mouth with wide, watering eyes while Cheon Bongsu glares sideways at him. Final frame: held on the young soldier with both hands clamped over his mouth and Cheon Bongsu's stern round face beside him, all mouths closed or covered.

[Visual and Camera Treatment]
All shots at standing eye level from the center of the storehouse along a single action line, keeping Han Igyeom on the left, Cheon Bongsu and the straw sacks in the center, and Jo Yun on the right near the doorway. Camera on a tripod and locked off in every shot except the dolly-in at 22-26s. Faces fill a large part of the frame in every shot, using only medium shots, medium two-shots, and medium close-ups. Lighting for this location: angled shafts of cool morning daylight enter through the open wooden storehouse doorway and high wall slats, cutting across the dusty interior and illuminating the faces and straw sacks.

[Audio]
No BGM; only ambient and action sounds: <heavy straw rice sacks thudding onto wooden floorboards>, <startled murmurs from soldiers>, <wet ink brush stroking coarse ledger paper>, <a sudden snort of laughter muffled by two hands clapping over a mouth>. Han Igyeom speaks Korean in a deep young male voice, but with the hesitant, overly polite tone of a tired middle-aged office worker. Cheon Bongsu speaks Korean in a loud, gruff, earnest voice of a stocky man in his forties. Jo Yun speaks Korean in a smooth, soft, measured tenor, calm and courteous. Only the man speaking in each shot moves his mouth; the others keep their mouths closed.

[Maintain Consistency]
@Image 1 is Han Igyeom, @Image 2 is Cheon Bongsu, @Image 3 is Jo Yun, @Image 4 is the wooden grain storehouse. Keep all three men's faces, hairstyles, builds and clothing identical to their references, including Han Igyeom's topknot, neatly trimmed black beard, thin pale scar on the left eyebrow, black cheollik robe and dark brown studded leather lamellar vest, Cheon Bongsu's black horsehair headband (manggeon), short dense black mustache and brown leather lamellar armor, and Jo Yun's pale grey-blue silk dopo robe, dark navy chest sash and small black lacquered brush case at the left hip. Keep the bare wooden wall exposed behind the single pulled-away row of sacks, the counted rows of straw sacks on the floor, Han Igyeom on the left, Cheon Bongsu in the center holding the ledger and brush, and Jo Yun on the right. Normal human eyes. Real-time natural speed, no slow motion. No subtitles, no on-screen text.
```

**효과음 자리**: 25초 "쥐가 백여든 석을 먹으면 소만 해졌겠소" 직후 병사가 웃음을 터뜨리기 직전 [효과음: 띠용]

## 클립 07B — 군량 창고, 대호의 도착 (24초)

**참조**: 1 한이겸 시트, 2 천봉수 시트, 3 조윤 시트, 4 군량 창고

```
[Generation Goal]
Live-action Korean historical comedy drama, real-time natural speed: inside the wooden grain storehouse with the missing grain exposed, the suspicious secretary steps close to question the general's sudden skill with numbers, a horn blasts outside announcing the dreaded commander Kim Jongseo's arrival, and the general quietly shuts his eyes at the worst possible timing for a head-office audit. All acting is grounded and understated, like a naturalistic Korean TV drama. The camera stays at eye level.

[Reference Material Roles]
@Image 1 defines only Han Igyeom's face, hairstyle, build and clothing. Do not copy its framing, grey background or panel layout.
@Image 2 defines only Cheon Bongsu's face, hairstyle, build and clothing. Do not copy its framing, grey background or panel layout.
@Image 3 defines only Jo Yun's face, hairstyle, build and clothing. Do not copy its framing, grey background or panel layout.
@Image 4 defines only the wooden grain storehouse's walls, timber pillars, plank floor, and daylight shafts: the straw rice sacks now lie in low counted rows on the floor with the bare empty wooden wall exposed behind them. @Image 4 is a style reference only, not a fixed keyframe.

[Subjects and Relationships]
Han Igyeom corresponds to @Image 1: an original 28-year-old Korean man, 185 cm, broad-shouldered powerful warrior build with a thick chest and heavy muscular arms, short full black beard and mustache, neatly trimmed, a thin pale scar cuts vertically through the outer end of the left eyebrow, long black hair tied up in a traditional Joseon topknot, with a few loose strands falling beside the face, wearing a black heavy cotton cheollik military robe with a dark crimson inner lining showing at the collar, a dark brown leather lamellar vest with small iron studs over it, a wide black leather belt with a plain brass buckle, dark trousers tucked into black leather boots, and brown leather bracers on both forearms.
Cheon Bongsu corresponds to @Image 2: an original 45-year-old Korean man, 168 cm, short and stocky with a barrel chest, thick neck and strong short arms, round broad face with full ruddy sunburnt cheeks, a short dense black mustache and a sparse short goatee, short black hair tied in a small topknot, with a black woven horsehair headband (manggeon) across the forehead, wearing brown leather lamellar armor laced with dark cord over a dark grey cotton robe, a wide brown leather belt, dark grey trousers wrapped at the shins with off-white cloth leg bindings, and worn brown leather boots.
Jo Yun corresponds to @Image 3: an original 35-year-old Korean man, 176 cm, slender with an upright, composed posture, long narrow face with pale even skin and a few faint freckles across the bridge of the nose, narrow single-lidded dark eyes with a calm, unreadable gaze, thin lips set in a faint polite half-smile, a very thin, neatly trimmed mustache, black hair tied in a tidy topknot, wearing a pale grey-blue silk dopo scholar's robe with wide sleeves, a dark navy cord sash tied high at the chest, a white inner jacket collar visible at the neck, white beoseon socks, black taesahye shoes, and a small black lacquered brush case hanging from the sash at the left hip.
The top of Cheon Bongsu's head reaches only Han Igyeom's nose.
The top of Jo Yun's head reaches Han Igyeom's eyebrows.
The top of Cheon Bongsu's head reaches Jo Yun's eyes.
Han Igyeom wears the full dark lamellar armor coat over his black cheollik, helmet off, topknot visible. Han Igyeom always stands on the left side of the storehouse floor with the bare empty wooden storehouse wall and low rows of counted straw sacks behind him. Jo Yun always stands close in front of Han Igyeom on the right during 0-10s, facing left so the top of his head reaches Han Igyeom's eyebrows. Cheon Bongsu always stands to the right alongside two minor officers in brown leather armor, stepping close to Han Igyeom's right side at 15s and looking up so the top of his head reaches only Han Igyeom's nose.

[Event Script]
0-2s: Medium two-shot at eye level framing Han Igyeom on the left and Jo Yun on the right among the low rows of counted straw sacks. Jo Yun takes one measured step closer to Han Igyeom, hands tucked in his wide grey-blue sleeves, his narrow eyes fixed on Han Igyeom's face. Both mouths closed.
2-6s: Tight medium two-shot at eye level of Han Igyeom on the left and Jo Yun standing close on the right so the top of Jo Yun's head reaches Han Igyeom's eyebrows. A faint sheen of sweat shows at Han Igyeom's left temple; he holds Jo Yun's gaze with a still, guarded face as Jo Yun leans in slightly. At 2s Jo Yun says in Seoul-accented Korean, in a low, probing tone: {장군님께서 언제부터 셈에 그리 밝으셨습니까.}
6-10s: Medium shot at eye level of Cheon Bongsu and two minor officers in brown leather armor turning their heads toward the bright open storehouse doorway on the right as a long horn blast echoes from outside. Their hands move to the hilts of the swords at their waists. At 7s an off-screen soldier's voice shouts from outside in Seoul-accented Korean, in an alarmed, urgent tone: {기병이다! 성문으로 온다!} All on-screen mouths stay closed.
10-15s: Same medium shot of Cheon Bongsu and the two officers facing the sunlit doorway. Hearing the second shout from outside, their hands slowly come off their sword hilts and they exchange a brief, uneasy glance, their faces going quiet and tense. At 10s the off-screen soldier's voice shouts from outside in Seoul-accented Korean, in a ringing, breathless tone: {아니다! 우리 깃발이다! 도절제사 영감이시다!} All on-screen mouths stay closed.
15-19s: Medium two-shot at eye level of Han Igyeom on the left and Cheon Bongsu stepping right up beside him on the right, tilting his head back so the top of his head reaches only Han Igyeom's nose. At 15s Cheon Bongsu says in Seoul-accented Korean, in a hushed, uneasy tone: {장군님, 대호께서 오셨습니다. 하필 오늘.}
19-24s: The key moment. Starting from a medium close-up of Han Igyeom with the bare empty wooden wall behind the low counted sacks visible over his shoulder, the camera dollies in across this whole range to a tight close-up of his face. Han Igyeom glances back over his shoulder at the empty space in the storehouse, turns forward, closes his eyes for a moment and lets out a slow breath through his nose, his face otherwise still. At 19s he says in Seoul-accented Korean, in a low, weary, resigned middle-aged office worker tone, almost under his breath: {본사 감사가 왜 하필 지금.} Final frame: held for the last two seconds on Han Igyeom with his eyes closed and a faint sheen of sweat at his temple, mouth closed.

[Visual and Camera Treatment]
All shots at standing eye level from the center of the storehouse along a single action line, keeping Han Igyeom on the left and Jo Yun and Cheon Bongsu on the right. Camera on a tripod and locked off in every shot except the dolly-in at 19-24s. Faces fill a large part of the frame in every shot, using only medium shots, medium two-shots, and close-ups. Acting stays natural and restrained: small, realistic facial expressions and gestures, no exaggerated or comedic mugging. Lighting for this location: angled shafts of cool morning daylight enter through the open wooden storehouse doorway and high wall slats, cutting across the dusty interior and illuminating the faces and straw sacks.

[Audio]
No BGM; only ambient and action sounds: <a long, low horn blast echoing from outside the fortress>, <distant galloping horse hooves outside>, <leather armor rustling and metal sword guards clicking as officers grip their hilts>. Jo Yun speaks Korean in a smooth, soft, measured tenor, calm and courteous, lowered to a quiet probe. An off-screen soldier shouts from outside in a high, urgent young male voice. Cheon Bongsu speaks Korean in a loud, gruff, earnest voice of a stocky man in his forties, hushed in dread. Han Igyeom speaks Korean in a deep young male voice, but with the hesitant, overly polite tone of a tired middle-aged office worker. Only the man speaking in each shot moves his mouth; when the off-screen soldier shouts outside at 6-15s, all on-screen men keep their mouths closed.

[Maintain Consistency]
@Image 1 is Han Igyeom, @Image 2 is Cheon Bongsu, @Image 3 is Jo Yun, @Image 4 is the wooden grain storehouse. Keep all three men's faces, hairstyles, builds and clothing identical to their references, including Han Igyeom's topknot, neatly trimmed black beard, thin pale scar on the left eyebrow, black cheollik robe and dark brown studded leather lamellar vest, Cheon Bongsu's black horsehair headband (manggeon), short dense black mustache and brown leather lamellar armor, and Jo Yun's pale grey-blue silk dopo robe, dark navy chest sash and small black lacquered brush case at the left hip. Keep the bare wooden storehouse wall exposed behind the low rows of counted straw sacks, Han Igyeom on the left, Jo Yun and Cheon Bongsu on the right, and the camera on the same side of the action line. Normal human eyes. Real-time natural speed, no slow motion. No subtitles, no on-screen text.
```

## 클립 07C — 군량 창고, 아침 (24초)

**참조**: 1 한이겸 시트, 2 천봉수 시트, 3 조윤 시트, 4 군량 창고

```
[Generation Goal]
Live-action Korean historical comedy drama, real-time natural speed, 24 seconds (576 frames at 24 fps): one event — inside the wooden fortress grain storehouse as approaching hoofbeats echo from outside, the secretary orders two soldiers to stuff empty straw sacks to fake the front row, and the general raises a hand to stop them, calling it fraud. Exactly five men are visible: Han Igyeom, Cheon Bongsu, Jo Yun, and two background soldiers. Eye-level camera, locked off except one dolly-in at 16-20s. No BGM.

[Reference Material Roles]
@Image 1 defines only Han Igyeom's face, hairstyle, build and clothing. Do not copy its framing, grey background or panel layout. His facial expression comes from this shot description, not from @Image 1.
@Image 2 defines only Cheon Bongsu's face, hairstyle, build and clothing. Do not copy its framing, grey background or panel layout. His facial expression comes from this shot description, not from @Image 2.
@Image 3 defines only Jo Yun's face, hairstyle, build and clothing. Do not copy its framing, grey background or panel layout. His facial expression comes from this shot description, not from @Image 3.
@Image 4 defines only the wooden grain storehouse's walls, timber pillars, plank floor, and daylight shafts: the straw rice sacks lie in low counted rows on the floor with the bare empty wooden wall exposed behind them and a small pile of empty straw sacks and loose straw near the right pillar. @Image 4 is a style reference only, not a fixed keyframe.

[Subjects and Relationships]
Han Igyeom corresponds to @Image 1: an original 28-year-old Korean man, 185 cm, broad-shouldered powerful warrior build with a thick chest and heavy muscular arms, short full black beard and mustache, neatly trimmed, a thin pale scar cuts vertically through the outer end of the left eyebrow, long black hair tied up in a traditional Joseon topknot, with a few loose strands falling beside the face, wearing a black heavy cotton cheollik military robe with a dark crimson inner lining showing at the collar, a dark brown leather lamellar vest with small iron studs over it, a wide black leather belt with a plain brass buckle, dark trousers tucked into black leather boots, and brown leather bracers on both forearms.
Cheon Bongsu corresponds to @Image 2: an original 45-year-old Korean man, 168 cm, short and stocky with a barrel chest, thick neck and strong short arms, round broad face with full ruddy sunburnt cheeks, a short dense black mustache and a sparse short goatee, short black hair tied in a small topknot, with a black woven horsehair headband (manggeon) across the forehead, wearing brown leather lamellar armor laced with dark cord over a dark grey cotton robe, a wide brown leather belt, dark grey trousers wrapped at the shins with off-white cloth leg bindings, and worn brown leather boots.
Jo Yun corresponds to @Image 3: an original 35-year-old Korean man, 176 cm, slender with an upright, composed posture, long narrow face with pale even skin and a few faint freckles across the bridge of the nose, narrow single-lidded dark eyes with a calm, unreadable gaze, thin lips set in a faint polite half-smile, a very thin, neatly trimmed mustache, black hair tied in a tidy topknot, wearing a pale grey-blue silk dopo scholar's robe with wide sleeves, a dark navy cord sash tied high at the chest, a white inner jacket collar visible at the neck, white beoseon socks, black taesahye shoes, and a small black lacquered brush case hanging from the sash at the left hip.
Han Igyeom wears the full dark lamellar armor coat over his black cheollik, helmet off, topknot visible, the same armor as in the previous scenes.
The top of Cheon Bongsu's head reaches only Han Igyeom's nose.
The top of Jo Yun's head reaches Han Igyeom's eyebrows.
The top of Cheon Bongsu's head reaches Jo Yun's eyes.
Han Igyeom always stands on the left side of the storehouse floor with the bare empty wooden wall behind him. Cheon Bongsu always stands in the center beside the low counted rows of straw sacks, holding the open paper ledger in his left hand and an inked brush in his right hand. Jo Yun always stands on the right near the storehouse doorway. Two background soldiers in plain grey cotton uniforms and cloth headbands always stand behind the low sacks on the right with their faces in profile. All faces have dry skin.

[Event Script]
0-2s: 50mm medium shot at eye level, camera locked off, framing Han Igyeom on the left, Cheon Bongsu in the center holding the ledger and brush, and Jo Yun on the right near the doorway. Jo Yun steps half a pace toward the two background soldiers on the right and gestures with his right hand toward the empty straw sacks on the floor. All mouths closed.
2-7s: 85mm medium close-up of Jo Yun on the right, camera locked off, looking right toward the two soldiers, not at the lens. At 2s, on-screen, Jo Yun says (speaking in Korean, low and brisk, clear, crisp pronunciation): "빈 가마니에 짚을 채워 앞줄만 다시 메워라. 어서."
7-10s: 50mm medium shot at eye level, camera locked off, framing Han Igyeom on the left and the two soldiers bending on the right to reach for the empty straw sacks. Han Igyeom raises his right hand to chest height, palm forward, stopping the soldiers before their hands lift the sacks. At 7.5s, on-screen, Han Igyeom says (speaking in Korean, firm and steady, clear, crisp pronunciation), looking right toward the soldiers: "손대지 마시오."
10-16s: 85mm medium close-up of Jo Yun on the right, camera locked off. Jo Yun turns his head left toward Han Igyeom, his brows drawing together slightly as he looks at Han Igyeom, not at the lens. At 10s, on-screen, Jo Yun says (speaking in Korean, low and urgent, clear, crisp pronunciation): "장군님, 도절제사 영감이십니다. 빈자리를 보이면 끝장입니다."
16-20s: The key moment. Starting from a 50mm medium close-up of Han Igyeom on the left with the bare wooden wall behind him, the camera dollies in slowly to an 85mm close-up across this whole range; this is the only camera move in the clip. Han Igyeom lowers his right hand to his side and looks straight right at Jo Yun, his jaw set. At 16s, on-screen, Han Igyeom says (speaking in Korean, calm and matter-of-fact, clear, crisp pronunciation): "빈자리를 가짜로 채우면 그건 사기요."
20-24s: Same 85mm close-up of Han Igyeom on the left, camera locked off, his eyes fixed to the right on Jo Yun as his jaw tightens once and he blinks once. Final frame: held on Han Igyeom's steady face looking right toward Jo Yun, mouth closed.

[Visual and Camera Treatment]
All shots at standing eye level from the center of the storehouse along a single action line, never crossing the 180-degree line: Han Igyeom always on the left, Cheon Bongsu in the center, Jo Yun and the two soldiers on the right. 50mm for medium shots, 85mm for medium close-ups and close-ups; size changes happen by cutting, not zooming. Camera locked off on a tripod in every shot except the single dolly-in at 16-20s; no zoom, no pan, no tilt, no other push-in, no drift, no handheld shake, no gimbal sway, no whip pan, no crane, no speed ramp. Speakers look at each other, never into the lens. Faces fill a large part of the frame in every shot. Acting stays natural and restrained: small, realistic facial expressions and gestures, no exaggerated or comedic mugging. All Korean dialogue is pronounced clearly at a natural speaking pace, never mumbled or rushed. Lighting for this location: angled shafts of cool morning daylight enter through the open wooden storehouse doorway and high wall slats, cutting across the dusty interior and illuminating the faces and straw sacks.

[Audio]
No BGM; only ambient and action sounds: <approaching horse hoofbeats and rhythmic war drums from far outside the storehouse doorway on the right, growing louder>, <coarse straw sacks rustling briefly as soldiers reach for them at 7s>, <leather bracer creaking softly as Han Igyeom raises his hand>. Han Igyeom speaks Korean in a deep young male voice, but with the hesitant, overly polite tone of a tired middle-aged office worker, firm and matter-of-fact. Jo Yun speaks Korean in a smooth, soft, measured tenor, calm and courteous, lowered in urgency. Only the man speaking in each shot moves his mouth; the others keep their mouths closed.

[Maintain Consistency]
@Image 1 is Han Igyeom, @Image 2 is Cheon Bongsu, @Image 3 is Jo Yun, @Image 4 is the wooden grain storehouse. Keep all three men's faces, hairstyles, builds and clothing identical to their references, including Han Igyeom's topknot, neatly trimmed black beard, thin pale scar on the left eyebrow, black cheollik robe and dark brown studded leather lamellar vest, Cheon Bongsu's black horsehair headband (manggeon), short dense black mustache and brown leather lamellar armor, and Jo Yun's pale grey-blue silk dopo robe, dark navy chest sash and small black lacquered brush case at the left hip. Keep the bare wooden wall exposed behind the low rows of counted straw sacks, Han Igyeom on the left, Cheon Bongsu in the center, and Jo Yun on the right. Exactly five men are visible; no other person appears. Dry skin on all faces. Camera locked off except the one dolly-in. No BGM. Normal human eyes. Real-time natural speed, no slow motion. No subtitles, no on-screen text.
```

**속마음**

| 시점(초) | 화면 | 박만수 속마음 |
|---|---|---|
| 20–24초 | 조윤을 바라보는 한이겸의 굳은 얼굴 클로즈업 (입 다묾) | "감사 나왔는데 분식회계를 하라고? 걸리면 내가 독박이지." |

---

## 클립 07D — 군량 창고, 아침 (19초)

**참조**: 1 한이겸 시트, 2 천봉수 시트, 3 조윤 시트, 4 군량 창고

**검수 메모**: 아르곤 초안(30초)은 대사 5줄 약 110음절이 30초에 몰려 1초 4음절을 넘었다. 07D(조윤 협박·천봉수 회유)와 07D2(자진 신고·브리핑)로 나눔.

```
[Generation Goal]
Live-action Korean historical comedy drama, real-time natural speed, 19 seconds (456 frames at 24 fps): one event — inside the wooden grain storehouse, the secretary quietly warns the general that his own seal is on the monthly grain reports, and the stocky officer begs him to cover up the shortage. Exactly three men are visible: Han Igyeom, Cheon Bongsu, and Jo Yun. Eye-level camera, locked off in every shot. No BGM.

[Reference Material Roles]
@Image 1 defines only Han Igyeom's face, hairstyle, build and clothing. Do not copy its framing, grey background or panel layout. His facial expression comes from this shot description, not from @Image 1.
@Image 2 defines only Cheon Bongsu's face, hairstyle, build and clothing. Do not copy its framing, grey background or panel layout. His facial expression comes from this shot description, not from @Image 2.
@Image 3 defines only Jo Yun's face, hairstyle, build and clothing. Do not copy its framing, grey background or panel layout. His facial expression comes from this shot description, not from @Image 3.
@Image 4 defines only the wooden grain storehouse's walls, timber pillars, plank floor, and daylight shafts: the straw rice sacks lie in low counted rows on the floor with the bare empty wooden wall exposed behind them and the open storehouse doorway on the right. @Image 4 is a style reference only, not a fixed keyframe.

[Subjects and Relationships]
Han Igyeom corresponds to @Image 1: an original 28-year-old Korean man, 185 cm, broad-shouldered powerful warrior build with a thick chest and heavy muscular arms, short full black beard and mustache, neatly trimmed, a thin pale scar cuts vertically through the outer end of the left eyebrow, long black hair tied up in a traditional Joseon topknot, with a few loose strands falling beside the face, wearing a black heavy cotton cheollik military robe with a dark crimson inner lining showing at the collar, a dark brown leather lamellar vest with small iron studs over it, a wide black leather belt with a plain brass buckle, dark trousers tucked into black leather boots, and brown leather bracers on both forearms.
Cheon Bongsu corresponds to @Image 2: an original 45-year-old Korean man, 168 cm, short and stocky with a barrel chest, thick neck and strong short arms, round broad face with full ruddy sunburnt cheeks, a short dense black mustache and a sparse short goatee, short black hair tied in a small topknot, with a black woven horsehair headband (manggeon) across the forehead, wearing brown leather lamellar armor laced with dark cord over a dark grey cotton robe, a wide brown leather belt, dark grey trousers wrapped at the shins with off-white cloth leg bindings, and worn brown leather boots.
Jo Yun corresponds to @Image 3: an original 35-year-old Korean man, 176 cm, slender with an upright, composed posture, long narrow face with pale even skin and a few faint freckles across the bridge of the nose, narrow single-lidded dark eyes with a calm, unreadable gaze, thin lips set in a faint polite half-smile, a very thin, neatly trimmed mustache, black hair tied in a tidy topknot, wearing a pale grey-blue silk dopo scholar's robe with wide sleeves, a dark navy cord sash tied high at the chest, a white inner jacket collar visible at the neck, white beoseon socks, black taesahye shoes, and a small black lacquered brush case hanging from the sash at the left hip.
Han Igyeom wears the full dark lamellar armor coat over his black cheollik, helmet off, topknot visible, the same armor as in the previous scenes.
The top of Cheon Bongsu's head reaches only Han Igyeom's nose.
The top of Jo Yun's head reaches Han Igyeom's eyebrows.
The top of Cheon Bongsu's head reaches Jo Yun's eyes.
Han Igyeom always stands on the left side of the storehouse floor facing right. Cheon Bongsu always stands in the center beside Han Igyeom, holding the open paper ledger and brush. Jo Yun always stands on the right facing left toward Han Igyeom. All faces have dry skin.

[Event Script]
0-2s: 50mm medium two-shot at eye level, camera locked off, framing Han Igyeom on the left and Jo Yun on the right. Jo Yun takes one measured step closer to Han Igyeom so the top of Jo Yun's head reaches Han Igyeom's eyebrows, his hands resting at the edges of his wide grey-blue sleeves. Both mouths closed.
2-7s: 85mm medium close-up of Jo Yun on the right, camera locked off, leaning in slightly and looking left at Han Igyeom, not at the lens. At 2s, on-screen, Jo Yun says (speaking in Korean, low, quiet and measured, clear, crisp pronunciation): "달마다 올린 군량 보고서에 장군님 직인도 찍혀 있습니다."
7-11s: Same 85mm medium close-up of Jo Yun on the right, camera locked off, his narrow eyes fixed left on Han Igyeom. At 7s, on-screen, Jo Yun says (speaking in Korean, low and even, clear, crisp pronunciation): "백여든 석이 비면 소인만 죽는 게 아닙니다."
11-17s: 50mm medium two-shot at eye level, camera locked off, framing Han Igyeom on the left and Cheon Bongsu in the center tilting his head back to look up at Han Igyeom so the top of his head reaches only Han Igyeom's nose. At 11s, on-screen, Cheon Bongsu says (speaking in Korean, quiet and earnest, at a natural pace with clear, crisp pronunciation): "장군님, 전시 군량 축내는 건 참수입니다. 일단 덮으시지요."
17-19s: The key moment. 85mm medium close-up of Han Igyeom on the left, camera locked off, looking down at the open ledger in Cheon Bongsu's hands in the center, then back up at Jo Yun on the right, not at the lens; his jaw tightens once. Final frame: held on Han Igyeom's still face looking right toward Jo Yun, mouth closed.

[Visual and Camera Treatment]
All shots at standing eye level from the center of the storehouse along a single action line, never crossing the 180-degree line: Han Igyeom on the left, Cheon Bongsu in the center, Jo Yun on the right. 50mm for medium two-shots and medium close-ups, 85mm for close-ups; size changes happen by cutting, not zooming. Camera locked off on a tripod in every shot; no dolly, no zoom, no pan, no tilt, no push-in, no drift, no handheld shake, no gimbal sway, no whip pan, no crane, no speed ramp. Speakers look at each other, never into the lens. Faces fill a large part of the frame in every shot. Acting stays natural and restrained: small, realistic facial expressions and gestures, no exaggerated or comedic mugging. All Korean dialogue is pronounced clearly at a natural speaking pace, never mumbled or rushed. Lighting for this location: angled shafts of cool morning daylight enter through the open wooden storehouse doorway and high wall slats, cutting across the dusty interior and illuminating the faces and straw sacks.

[Audio]
No BGM; only ambient and action sounds: <heavy horse hoofbeats and war drums outside the storehouse doorway on the right>. Han Igyeom speaks Korean in a deep young male voice, but with the hesitant, overly polite tone of a tired middle-aged office worker. Cheon Bongsu speaks Korean in a loud, gruff, earnest voice of a stocky man in his forties, lowered in urgency. Jo Yun speaks Korean in a smooth, soft, measured tenor, calm and courteous, lowered to a quiet warning. Only the man speaking in each shot moves his mouth; the others keep their mouths closed.

[Maintain Consistency]
@Image 1 is Han Igyeom, @Image 2 is Cheon Bongsu, @Image 3 is Jo Yun, @Image 4 is the wooden grain storehouse. Keep all three men's faces, hairstyles, builds and clothing identical to their references, including Han Igyeom's topknot, neatly trimmed black beard, thin pale scar on the left eyebrow, black cheollik robe and dark brown studded leather lamellar vest, Cheon Bongsu's black horsehair headband (manggeon), short dense black mustache and brown leather lamellar armor, and Jo Yun's pale grey-blue silk dopo robe, dark navy chest sash and small black lacquered brush case at the left hip. Keep the bare wooden wall exposed behind the low rows of counted straw sacks, Han Igyeom on the left, Cheon Bongsu in the center, and Jo Yun on the right. Exactly three men are visible; no other person appears. Dry skin on all faces. Camera locked off in every shot. No BGM. Normal human eyes. Real-time natural speed, no slow motion. No subtitles, no on-screen text.
```

---

## 클립 07D2 — 군량 창고, 아침 (20초)

**참조**: 1 한이겸 시트, 2 천봉수 시트, 3 조윤 시트, 4 군량 창고

```
[Generation Goal]
Live-action Korean historical comedy drama, real-time natural speed, 20 seconds (480 frames at 24 fps): one event — inside the wooden grain storehouse, the general takes the ledger to self-report the shortage, announces he will brief the commander himself, and walks out while the secretary's hand closes into a fist. Exactly three men are visible: Han Igyeom, Cheon Bongsu, and Jo Yun. Eye-level camera, locked off except one dolly-in at 10-17s. No BGM.

[Reference Material Roles]
@Image 1 defines only Han Igyeom's face, hairstyle, build and clothing. Do not copy its framing, grey background or panel layout. His facial expression comes from this shot description, not from @Image 1.
@Image 2 defines only Cheon Bongsu's face, hairstyle, build and clothing. Do not copy its framing, grey background or panel layout. His facial expression comes from this shot description, not from @Image 2.
@Image 3 defines only Jo Yun's face, hairstyle, build and clothing. Do not copy its framing, grey background or panel layout. His facial expression comes from this shot description, not from @Image 3.
@Image 4 defines only the wooden grain storehouse's walls, timber pillars, plank floor, and daylight shafts: the straw rice sacks lie in low counted rows on the floor with the bare empty wooden wall exposed behind them and the open storehouse doorway on the right. @Image 4 is a style reference only, not a fixed keyframe.

[Subjects and Relationships]
Han Igyeom corresponds to @Image 1: an original 28-year-old Korean man, 185 cm, broad-shouldered powerful warrior build with a thick chest and heavy muscular arms, short full black beard and mustache, neatly trimmed, a thin pale scar cuts vertically through the outer end of the left eyebrow, long black hair tied up in a traditional Joseon topknot, with a few loose strands falling beside the face, wearing a black heavy cotton cheollik military robe with a dark crimson inner lining showing at the collar, a dark brown leather lamellar vest with small iron studs over it, a wide black leather belt with a plain brass buckle, dark trousers tucked into black leather boots, and brown leather bracers on both forearms.
Cheon Bongsu corresponds to @Image 2: an original 45-year-old Korean man, 168 cm, short and stocky with a barrel chest, thick neck and strong short arms, round broad face with full ruddy sunburnt cheeks, a short dense black mustache and a sparse short goatee, short black hair tied in a small topknot, with a black woven horsehair headband (manggeon) across the forehead, wearing brown leather lamellar armor laced with dark cord over a dark grey cotton robe, a wide brown leather belt, dark grey trousers wrapped at the shins with off-white cloth leg bindings, and worn brown leather boots.
Jo Yun corresponds to @Image 3: an original 35-year-old Korean man, 176 cm, slender with an upright, composed posture, long narrow face with pale even skin and a few faint freckles across the bridge of the nose, narrow single-lidded dark eyes with a calm, unreadable gaze, thin lips set in a faint polite half-smile, a very thin, neatly trimmed mustache, black hair tied in a tidy topknot, wearing a pale grey-blue silk dopo scholar's robe with wide sleeves, a dark navy cord sash tied high at the chest, a white inner jacket collar visible at the neck, white beoseon socks, black taesahye shoes, and a small black lacquered brush case hanging from the sash at the left hip.
Han Igyeom wears the full dark lamellar armor coat over his black cheollik, helmet off, topknot visible, the same armor as in the previous scenes.
The top of Cheon Bongsu's head reaches only Han Igyeom's nose.
The top of Jo Yun's head reaches Han Igyeom's eyebrows.
The top of Cheon Bongsu's head reaches Jo Yun's eyes.
Han Igyeom always stands on the left side of the storehouse floor facing right until he walks out past the right edge at 17-19s. Cheon Bongsu always stands in the center beside Han Igyeom, holding the open paper ledger and brush until Han Igyeom takes them at 0-2s. Jo Yun always stands on the right facing left toward Han Igyeom. All faces have dry skin.

[Event Script]
0-2s: 50mm medium two-shot at eye level, camera locked off, framing Han Igyeom on the left and Cheon Bongsu in the center holding the open paper ledger and brush. Han Igyeom reaches out with both hands, then takes the ledger and brush from Cheon Bongsu's hands. Both mouths closed.
2-7s: Same 50mm medium two-shot, camera locked off, Han Igyeom on the left holding the ledger, Cheon Bongsu in the center looking up at him. At 2s, on-screen, Han Igyeom says (speaking in Korean, calm and matter-of-fact, at a natural pace with clear, crisp pronunciation), looking down at Cheon Bongsu: "숨기다 걸리면 가중처벌이오. 자진 신고부터 해야지."
7-10s: 85mm medium close-up of Cheon Bongsu in the center, camera locked off, looking up left at Han Igyeom, not at the lens; he blinks once. At 7.5s, on-screen, Cheon Bongsu says (speaking in Korean, quiet and halting, with a short pause after the first word, clear, crisp pronunciation): "자진… 뭐, 뭐라 하셨습니까?"
10-17s: The key moment. Starting from a 50mm medium close-up of Han Igyeom on the left, the camera dollies in slowly to an 85mm close-up across this whole range; this is the only camera move in the clip. Han Igyeom folds the paper ledger shut, then tucks it under his left arm like an office clipboard. At 10.5s, on-screen, Han Igyeom says (speaking in Korean, brisk and businesslike at a natural pace, the last two words lower and slower, clear, crisp pronunciation), looking right toward Jo Yun: "창고 문 활짝 열어 두시오. 내가 직접 브리핑하겠소. 아니, 고하겠소!"
17-20s: 85mm medium close-up of Jo Yun standing on the right, camera locked off, as Han Igyeom's shoulder passes out of frame to the right toward the open doorway. The faint half-smile leaves Jo Yun's lips, and his right hand at the edge of his wide grey-blue sleeve closes into a fist. Final frame: held on Jo Yun's unsmiling face and his closed fist at the edge of his sleeve, mouth closed.

[Visual and Camera Treatment]
All shots at standing eye level from the center of the storehouse along a single action line, never crossing the 180-degree line: Han Igyeom on the left, Cheon Bongsu in the center, Jo Yun on the right. 50mm for medium two-shots and medium close-ups, 85mm for close-ups; size changes happen by cutting, not zooming. Camera locked off on a tripod in every shot except the single dolly-in at 10-17s; no zoom, no pan, no tilt, no other push-in, no drift, no handheld shake, no gimbal sway, no whip pan, no crane, no speed ramp. Speakers look at each other, never into the lens. Faces fill a large part of the frame in every shot. Acting stays natural and restrained: small, realistic facial expressions and gestures, no exaggerated or comedic mugging. All Korean dialogue is pronounced clearly at a natural speaking pace, never mumbled or rushed. Lighting for this location: angled shafts of cool morning daylight enter through the open wooden storehouse doorway and high wall slats, cutting across the dusty interior and illuminating the faces and straw sacks.

[Audio]
No BGM; only ambient and action sounds: <heavy horse hoofbeats and war drums outside the storehouse doorway on the right>, <paper ledger pages folding shut at 10s>, <leather boots stepping across wooden floorboards at 17-19s>. Han Igyeom speaks Korean in a deep young male voice, but with the hesitant, overly polite tone of a tired middle-aged office worker. Cheon Bongsu speaks Korean in a loud, gruff, earnest voice of a stocky man in his forties, lowered in urgency. Jo Yun speaks Korean in a smooth, soft, measured tenor, calm and courteous, lowered to a quiet warning. Only the man speaking in each shot moves his mouth; the others keep their mouths closed.

[Maintain Consistency]
@Image 1 is Han Igyeom, @Image 2 is Cheon Bongsu, @Image 3 is Jo Yun, @Image 4 is the wooden grain storehouse. Keep all three men's faces, hairstyles, builds and clothing identical to their references, including Han Igyeom's topknot, neatly trimmed black beard, thin pale scar on the left eyebrow, black cheollik robe and dark brown studded leather lamellar vest, Cheon Bongsu's black horsehair headband (manggeon), short dense black mustache and brown leather lamellar armor, and Jo Yun's pale grey-blue silk dopo robe, dark navy chest sash and small black lacquered brush case at the left hip. Keep the bare wooden wall exposed behind the low rows of counted straw sacks, Han Igyeom on the left, Cheon Bongsu in the center, and Jo Yun on the right. Exactly three men are visible; no other person appears. Dry skin on all faces. Camera locked off except the one dolly-in. No BGM. Normal human eyes. Real-time natural speed, no slow motion. No subtitles, no on-screen text.
```

**효과음 자리**: 7초 "자진 신고부터 해야지." 직후 [효과음: 정적]

---

## 클립 07E — 성문 안 마당, 아침 (28초)

**참조**: 1 한이겸 시트, 2 천봉수 시트, 3 조윤 시트, 4 성문 안 마당 아침

```
[Generation Goal]
Live-action Korean historical comedy drama, real-time natural speed, 28 seconds (672 frames at 24 fps): one event — in the snow-covered fortress courtyard before the closed main gate, the general waits with the grain ledger under his arm like a clipboard while his officer warns him that a nearby commander was flogged twenty strokes and dismissed over a single wrong line in a ledger. Exactly three men are visible: Jo Yun, Han Igyeom, and Cheon Bongsu. Eye-level camera, locked off except one dolly-in at 25-28s. No BGM.

[Reference Material Roles]
@Image 1 defines only Han Igyeom's face, hairstyle, build and clothing. Do not copy its framing, grey background or panel layout. His facial expression comes from this shot description, not from @Image 1.
@Image 2 defines only Cheon Bongsu's face, hairstyle, build and clothing. Do not copy its framing, grey background or panel layout. His facial expression comes from this shot description, not from @Image 2.
@Image 3 defines only Jo Yun's face, hairstyle, build and clothing. Do not copy its framing, grey background or panel layout. His facial expression comes from this shot description, not from @Image 3.
@Image 4 defines only the fortress gate courtyard's structures, ground and morning light: the closed heavy wooden fortress gate with its thick wooden crossbar and gatehouse on the left, the snow-covered courtyard and stone wall with banners in the center, and the open wooden grain storehouse on the right with a few low rows of straw sacks at the threshold and the bare empty wooden wall visible inside. @Image 4 is a style reference only, not a fixed keyframe.

[Subjects and Relationships]
Han Igyeom corresponds to @Image 1: an original 28-year-old Korean man, 185 cm, broad-shouldered powerful warrior build with a thick chest and heavy muscular arms, short full black beard and mustache, neatly trimmed, a thin pale scar cuts vertically through the outer end of the left eyebrow, long black hair tied up in a traditional Joseon topknot, with a few loose strands falling beside the face, wearing a black heavy cotton cheollik military robe with a dark crimson inner lining showing at the collar, a dark brown leather lamellar vest with small iron studs over it, a wide black leather belt with a plain brass buckle, dark trousers tucked into black leather boots, and brown leather bracers on both forearms.
Cheon Bongsu corresponds to @Image 2: an original 45-year-old Korean man, 168 cm, short and stocky with a barrel chest, thick neck and strong short arms, round broad face with full ruddy sunburnt cheeks, a short dense black mustache and a sparse short goatee, short black hair tied in a small topknot, with a black woven horsehair headband (manggeon) across the forehead, wearing brown leather lamellar armor laced with dark cord over a dark grey cotton robe, a wide brown leather belt, dark grey trousers wrapped at the shins with off-white cloth leg bindings, and worn brown leather boots.
Jo Yun corresponds to @Image 3: an original 35-year-old Korean man, 176 cm, slender with an upright, composed posture, long narrow face with pale even skin and a few faint freckles across the bridge of the nose, narrow single-lidded dark eyes with a calm, unreadable gaze, thin lips set in a faint polite half-smile, a very thin, neatly trimmed mustache, black hair tied in a tidy topknot, wearing a pale grey-blue silk dopo scholar's robe with wide sleeves, a dark navy cord sash tied high at the chest, a white inner jacket collar visible at the neck, white beoseon socks, black taesahye shoes, and a small black lacquered brush case hanging from the sash at the left hip.
Han Igyeom wears the full dark lamellar armor coat over his black cheollik, helmet off, topknot visible, the same armor as in the previous scenes.
The top of Cheon Bongsu's head reaches only Han Igyeom's nose.
The top of Jo Yun's head reaches Han Igyeom's eyebrows.
The top of Cheon Bongsu's head reaches Jo Yun's eyes.
Han Igyeom always stands in the center of the snow-covered courtyard facing left toward the closed wooden fortress gate, with the closed paper ledger tucked under his left arm and the open grain storehouse behind him on the right. Cheon Bongsu always stands on the right next to Han Igyeom, tilting his head back so the top of his head reaches only Han Igyeom's nose. Jo Yun always stands half a pace behind on the left side of the frame with his hands inside his wide sleeves. All faces have dry skin.

[Event Script]
0-4s: 50mm medium shot at eye level, camera locked off, framing Jo Yun on the left, Han Igyeom in the center with the paper ledger tucked under his left arm, and Cheon Bongsu on the right with the open grain storehouse visible behind them. As horse hoofbeats outside the closed gate on the left come to a sudden stop, Han Igyeom brushes dust once off the front of his leather vest with his right hand and straightens his collar, looking left toward the gate. All mouths closed.
4-11s: 50mm medium two-shot at eye level, camera locked off, framing Han Igyeom in the center and Cheon Bongsu on the right tilting his head back to look up at Han Igyeom, not at the lens. At 4s, on-screen, Cheon Bongsu says (speaking in Korean, quiet and low, at a natural pace with clear, crisp pronunciation): "장군님, 영감께서 눈을 마주치시면 무조건 죽여 달라고 하십시오."
11-17s: 85mm medium close-up of Han Igyeom in the center, camera locked off, turning his head slightly right to look down at Cheon Bongsu, not at the lens. At 11s, on-screen, Han Igyeom says (speaking in Korean, polite modern office-worker tone at first, then correcting the final word in a firmer historical tone, clear, crisp pronunciation): "일하러 온 사람한테 왜 죽여 달라고 해요? 아니, 하느냐."
17-25s: 85mm medium close-up of Cheon Bongsu on the right, camera locked off, looking up left at Han Igyeom, not at the lens. At 17s, on-screen, Cheon Bongsu says (speaking in Korean, hushed and earnest at a natural pace, clear, crisp pronunciation): "지난달에 옆 진 첨절제사는 장부 한 줄 틀렸다고 곤장 스무 대에 파직당했습니다."
25-28s: The key moment. Starting from a 50mm medium close-up of Han Igyeom in the center with the open doorway and bare empty wooden wall of the grain storehouse visible behind his right shoulder, the camera dollies in slowly to an 85mm close-up across this whole range; this is the only camera move in the clip. Han Igyeom's right hand stops motionless on his leather belt and his jaw tightens once as he looks left toward the closed fortress gate. Final frame: held on Han Igyeom's still face with his right hand resting motionless on his belt and the ledger tucked under his left arm, mouth closed.

[Visual and Camera Treatment]
All shots at standing eye level in the courtyard along a single action line, never crossing the 180-degree line: the closed wooden gate and Jo Yun on the left, Han Igyeom in the center, Cheon Bongsu and the open grain storehouse on the right. 50mm for medium shots and medium two-shots, 85mm for medium close-ups and close-ups; size changes happen by cutting, not zooming. Camera locked off on a tripod in every shot except the single dolly-in at 25-28s; no zoom, no pan, no tilt, no other push-in, no drift, no handheld shake, no gimbal sway, no whip pan, no crane, no speed ramp. Speakers look at each other, never into the lens. Faces fill a large part of the frame in every shot. Acting stays natural and restrained: small, realistic facial expressions and gestures, no exaggerated or comedic mugging. All Korean dialogue is pronounced clearly at a natural speaking pace, never mumbled or rushed. Lighting for this location: crisp, bright morning sunlight slants across the snow-covered fortress courtyard from the gate side on the left, casting clean shadows on the stone ground and illuminating the faces and wooden storehouse evenly.

[Audio]
No BGM; only ambient and action sounds: <galloping horse hoofbeats outside the heavy wooden gate on the left coming to a halt in the snow at 0-2s>, <a horse snorting once beyond the gate>, <light cloth rustle as Han Igyeom brushes his chest and adjusts his collar at 1-3s>, <cold morning wind brushing the courtyard banners>. Han Igyeom speaks Korean in a deep young male voice, but with the hesitant, overly polite tone of a tired middle-aged office worker. Cheon Bongsu speaks Korean in a loud, gruff, earnest voice of a stocky man in his forties, lowered to a hushed murmur. Only the man speaking in each shot moves his mouth; the others keep their mouths closed.

[Maintain Consistency]
@Image 1 is Han Igyeom, @Image 2 is Cheon Bongsu, @Image 3 is Jo Yun, @Image 4 is the fortress gate courtyard. Keep all three men's faces, hairstyles, builds and clothing identical to their references, including Han Igyeom's topknot, neatly trimmed black beard, thin pale scar on the left eyebrow, black cheollik robe and dark brown studded leather lamellar vest, Cheon Bongsu's black horsehair headband (manggeon), short dense black mustache and brown leather lamellar armor, and Jo Yun's pale grey-blue silk dopo robe, dark navy chest sash and small black lacquered brush case at the left hip. Keep the closed wooden gate on the left, the open grain storehouse on the right, Jo Yun on the left, Han Igyeom in the center with the ledger under his left arm, and Cheon Bongsu on the right. Exactly three men are visible; no other person appears. Dry skin on all faces. Camera locked off except the one dolly-in. No BGM. Normal human eyes. Real-time natural speed, no slow motion. No subtitles, no on-screen text.
```

**속마음**

| 시점(초) | 화면 | 박만수 속마음 |
|---|---|---|
| 1–4초 | 갑옷 가슴팍의 먼지를 털고 옷깃을 여미는 한이겸 얼굴 (입 다묾) | "김종서면 교과서에 나오는 그 북방의 대호 맞지." |
| 25–28초 | 허리띠 위에서 손이 멈추고 턱이 한 번 굳는 한이겸 얼굴 클로즈업 (입 다묾) | "한 줄에 곤장 스무 대? 여긴 백여든 석이 비는데." |

---

## 클립 07F — 성문 안 마당, 아침 (28초)

**참조**: 1 한이겸 시트, 2 천봉수 시트, 3 조윤 시트, 4 성문 안 마당 아침

```
[Generation Goal]
Live-action Korean historical comedy drama, real-time natural speed, 28 seconds (672 frames at 24 fps): one event — in the snow-covered fortress courtyard, the general rejects the secretary's plea to blame rats, rehearses a modern corporate audit greeting aloud while holding the ledger, and watches two soldiers lift the crossbar and swing the main fortress gate open. Exactly five men are visible: Jo Yun, Han Igyeom, Cheon Bongsu, and two gate soldiers. Eye-level camera, locked off except one dolly-in at 14-21s. No BGM.

[Reference Material Roles]
@Image 1 defines only Han Igyeom's face, hairstyle, build and clothing. Do not copy its framing, grey background or panel layout. His facial expression comes from this shot description, not from @Image 1.
@Image 2 defines only Cheon Bongsu's face, hairstyle, build and clothing. Do not copy its framing, grey background or panel layout. His facial expression comes from this shot description, not from @Image 2.
@Image 3 defines only Jo Yun's face, hairstyle, build and clothing. Do not copy its framing, grey background or panel layout. His facial expression comes from this shot description, not from @Image 3.
@Image 4 defines only the fortress gate courtyard's structures, ground and morning light: the heavy wooden fortress gate with its thick wooden crossbar and gatehouse on the left, the snow-covered courtyard and stone wall with banners in the center, and the open wooden grain storehouse on the right with a few low rows of straw sacks at the threshold and the bare empty wooden wall visible inside. @Image 4 is a style reference only, not a fixed keyframe.

[Subjects and Relationships]
Han Igyeom corresponds to @Image 1: an original 28-year-old Korean man, 185 cm, broad-shouldered powerful warrior build with a thick chest and heavy muscular arms, short full black beard and mustache, neatly trimmed, a thin pale scar cuts vertically through the outer end of the left eyebrow, long black hair tied up in a traditional Joseon topknot, with a few loose strands falling beside the face, wearing a black heavy cotton cheollik military robe with a dark crimson inner lining showing at the collar, a dark brown leather lamellar vest with small iron studs over it, a wide black leather belt with a plain brass buckle, dark trousers tucked into black leather boots, and brown leather bracers on both forearms.
Cheon Bongsu corresponds to @Image 2: an original 45-year-old Korean man, 168 cm, short and stocky with a barrel chest, thick neck and strong short arms, round broad face with full ruddy sunburnt cheeks, a short dense black mustache and a sparse short goatee, short black hair tied in a small topknot, with a black woven horsehair headband (manggeon) across the forehead, wearing brown leather lamellar armor laced with dark cord over a dark grey cotton robe, a wide brown leather belt, dark grey trousers wrapped at the shins with off-white cloth leg bindings, and worn brown leather boots.
Jo Yun corresponds to @Image 3: an original 35-year-old Korean man, 176 cm, slender with an upright, composed posture, long narrow face with pale even skin and a few faint freckles across the bridge of the nose, narrow single-lidded dark eyes with a calm, unreadable gaze, thin lips set in a faint polite half-smile, a very thin, neatly trimmed mustache, black hair tied in a tidy topknot, wearing a pale grey-blue silk dopo scholar's robe with wide sleeves, a dark navy cord sash tied high at the chest, a white inner jacket collar visible at the neck, white beoseon socks, black taesahye shoes, and a small black lacquered brush case hanging from the sash at the left hip.
Han Igyeom wears the full dark lamellar armor coat over his black cheollik, helmet off, topknot visible, the same armor as in the previous scenes.
The top of Cheon Bongsu's head reaches only Han Igyeom's nose.
The top of Jo Yun's head reaches Han Igyeom's eyebrows.
The top of Cheon Bongsu's head reaches Jo Yun's eyes.
Jo Yun always stands on the left side of the center group. Han Igyeom always stands in the center of the courtyard facing left toward the fortress gate, holding the paper ledger. Cheon Bongsu always stands on the right next to Han Igyeom with the open grain storehouse behind him. Two background soldiers in plain grey cotton uniforms stand beside the wooden fortress gate on the far left with their faces in profile. All faces have dry skin.

[Event Script]
0-2s: 50mm medium two-shot at eye level, camera locked off, framing Jo Yun on the left and Han Igyeom in the center with the ledger tucked under his left arm. Jo Yun takes half a step closer to Han Igyeom while keeping his gaze toward the closed wooden gate on the left. Both mouths closed.
2-8s: 85mm medium close-up of Jo Yun on the left, camera locked off, looking left toward the gate as he speaks in a low voice toward Han Igyeom, not at the lens. At 2s, on-screen, Jo Yun says (speaking in Korean, low, quiet and measured, clear, crisp pronunciation): "장군님, 지금이라도 창고 문을 닫고 쥐 핑계를 대시지요."
8-14s: 85mm medium close-up of Han Igyeom in the center, camera locked off, glancing left at Jo Yun, not at the lens. At 8s, on-screen, Han Igyeom says (speaking in Korean, dry and matter-of-fact at a natural pace, clear, crisp pronunciation): "소만 한 쥐가 먹었다고 하면 곤장이 아니라 칼이 날아오겠소."
14-21s: The key moment. Starting from a 50mm medium close-up of Han Igyeom in the center, the camera dollies in slowly to an 85mm close-up across this whole range; this is the only camera move in the clip. Han Igyeom shifts the closed paper ledger from under his left arm into his right hand, looks left toward the gate, loosens his mouth once, and speaks as if rehearsing a formal company audit report. At 15s, on-screen, Han Igyeom says (speaking in Korean, polite and formal like an office manager practicing a presentation, clear, crisp pronunciation): "안녕하십니까, 도절제사님. 삭풍진 재고 감사 보고드리겠습니다."
21-24s: 85mm medium close-up of Cheon Bongsu on the right, camera locked off, tilting his head back and blinking once as he looks up left at Han Igyeom, not at the lens. At 21s, on-screen, Cheon Bongsu says (speaking in Korean, hushed and stammering, clear, crisp pronunciation): "가, 감… 뭐라 하셨습니까?"
24-28s: 50mm medium shot at eye level, camera locked off, framing the heavy wooden fortress gate on the left with Han Igyeom and Cheon Bongsu in the right foreground facing it. Two soldiers in grey cotton uniforms grip the thick wooden crossbar, lift it off its brackets, and pull both heavy wooden gate doors inward until the gate is fully open and bright morning sunlight pours across the courtyard. Final frame: held on the wide-open wooden fortress gate with bright morning sunlight streaming into the courtyard, all mouths closed.

[Visual and Camera Treatment]
All shots at standing eye level in the courtyard along a single action line, never crossing the 180-degree line: the wooden fortress gate and Jo Yun on the left, Han Igyeom in the center, Cheon Bongsu and the open grain storehouse on the right. 50mm for medium shots and medium two-shots, 85mm for medium close-ups and close-ups; size changes happen by cutting, not zooming. Camera locked off on a tripod in every shot except the single dolly-in at 14-21s; no zoom, no pan, no tilt, no other push-in, no drift, no handheld shake, no gimbal sway, no whip pan, no crane, no speed ramp. Speakers look at each other or toward the gate, never into the lens. Faces fill a large part of the frame in every shot. Acting stays natural and restrained: small, realistic facial expressions and gestures, no exaggerated or comedic mugging. All Korean dialogue is pronounced clearly at a natural speaking pace, never mumbled or rushed. Lighting for this location: crisp, bright morning sunlight slants across the snow-covered fortress courtyard from the gate side on the left, casting clean shadows on the stone ground and illuminating the faces and wooden storehouse evenly.

[Audio]
No BGM; only ambient and action sounds: <paper ledger shifting from arm to hand at 14s>, <heavy wooden crossbar lifting from iron brackets with a solid clunk at 24s>, <massive wooden gate hinges groaning open at 25-27s>. Jo Yun speaks Korean in a smooth, soft, measured tenor, calm and courteous, lowered to a quiet murmur. Han Igyeom speaks Korean in a deep young male voice, but with the hesitant, overly polite tone of a tired middle-aged office worker. Cheon Bongsu speaks Korean in a loud, gruff, earnest voice of a stocky man in his forties, hushed and stammering. Only the man speaking in each shot moves his mouth; the others keep their mouths closed.

[Maintain Consistency]
@Image 1 is Han Igyeom, @Image 2 is Cheon Bongsu, @Image 3 is Jo Yun, @Image 4 is the fortress gate courtyard. Keep all three men's faces, hairstyles, builds and clothing identical to their references, including Han Igyeom's topknot, neatly trimmed black beard, thin pale scar on the left eyebrow, black cheollik robe and dark brown studded leather lamellar vest, Cheon Bongsu's black horsehair headband (manggeon), short dense black mustache and brown leather lamellar armor, and Jo Yun's pale grey-blue silk dopo robe, dark navy chest sash and small black lacquered brush case at the left hip. Keep the wooden gate on the left, the open grain storehouse on the right, Jo Yun on the left, Han Igyeom in the center holding the ledger, and Cheon Bongsu on the right. Exactly five men are visible; no other person appears. Dry skin on all faces. Camera locked off except the one dolly-in. No BGM. Normal human eyes. Real-time natural speed, no slow motion. No subtitles, no on-screen text.
```

---

## 클립 07G — 성문 안 마당, 아침 (22초)

**참조**: 1 김종서 시트, 2 한이겸 시트, 3 천봉수 시트, 4 조윤 시트, 5 성문 안 마당 아침

```
[Generation Goal]
Live-action Korean historical comedy drama, real-time natural speed, 22 seconds (528 frames at 24 fps): one event — in the sunlit fortress courtyard, Commander Kim Jongseo walks in through the open gate and every officer kneels except the general, who gives a polite ninety-degree modern office bow before his officer yanks his robe hem down so his right knee hits the stone ground. Exactly four named men (Kim Jongseo, Han Igyeom, Cheon Bongsu, Jo Yun) and two background banner-bearers at the gate are visible. Eye-level camera, locked off except one dolly-in at 13-18s. No BGM.

[Reference Material Roles]
@Image 1 defines only Kim Jongseo's face, hairstyle, build and clothing. Do not copy its framing, grey background or panel layout. His facial expression comes from this shot description, not from @Image 1.
@Image 2 defines only Han Igyeom's face, hairstyle, build and clothing. Do not copy its framing, grey background or panel layout. His facial expression comes from this shot description, not from @Image 2.
@Image 3 defines only Cheon Bongsu's face, hairstyle, build and clothing. Do not copy its framing, grey background or panel layout. His facial expression comes from this shot description, not from @Image 3.
@Image 4 defines only Jo Yun's face, hairstyle, build and clothing. Do not copy its framing, grey background or panel layout. His facial expression comes from this shot description, not from @Image 4.
@Image 5 defines only the fortress gate courtyard's structures, ground and morning light: the wide-open heavy wooden fortress gate and gatehouse on the left, the snow-covered stone courtyard in the center, and the open wooden grain storehouse on the right with a few low rows of straw sacks at the threshold and the bare empty wooden wall visible inside. @Image 5 is a style reference only, not a fixed keyframe.

[Subjects and Relationships]
Kim Jongseo corresponds to @Image 1: a dignified 51-year-old Korean military commander of the early Joseon dynasty, 172 cm, broad-shouldered and upright with a powerful, compact build, square, weathered face with a strong jaw and deep lines at the eyes and forehead, sharp, piercing dark eyes under thick black eyebrows streaked with grey, a calm, unsmiling mouth, a neatly trimmed black beard and mustache streaked with grey, black hair with grey at the temples tied in a topknot under a black horsehair gat with a red tassel cord, wearing a deep crimson cheollik commander's robe with a black leather lamellar vest edged in brass, a wide black belt with a jade-ornamented buckle, black leather boots, and a sheathed long sword at his left hip.
Han Igyeom corresponds to @Image 2: an original 28-year-old Korean man, 185 cm, broad-shouldered powerful warrior build with a thick chest and heavy muscular arms, short full black beard and mustache, neatly trimmed, a thin pale scar cuts vertically through the outer end of the left eyebrow, long black hair tied up in a traditional Joseon topknot, with a few loose strands falling beside the face, wearing a black heavy cotton cheollik military robe with a dark crimson inner lining showing at the collar, a dark brown leather lamellar vest with small iron studs over it, a wide black leather belt with a plain brass buckle, dark trousers tucked into black leather boots, and brown leather bracers on both forearms.
Cheon Bongsu corresponds to @Image 3: an original 45-year-old Korean man, 168 cm, short and stocky with a barrel chest, thick neck and strong short arms, round broad face with full ruddy sunburnt cheeks, a short dense black mustache and a sparse short goatee, short black hair tied in a small topknot, with a black woven horsehair headband (manggeon) across the forehead, wearing brown leather lamellar armor laced with dark cord over a dark grey cotton robe, a wide brown leather belt, dark grey trousers wrapped at the shins with off-white cloth leg bindings, and worn brown leather boots.
Jo Yun corresponds to @Image 4: an original 35-year-old Korean man, 176 cm, slender with an upright, composed posture, long narrow face with pale even skin and a few faint freckles across the bridge of the nose, narrow single-lidded dark eyes with a calm, unreadable gaze, thin lips set in a faint polite half-smile, a very thin, neatly trimmed mustache, black hair tied in a tidy topknot, wearing a pale grey-blue silk dopo scholar's robe with wide sleeves, a dark navy cord sash tied high at the chest, a white inner jacket collar visible at the neck, white beoseon socks, black taesahye shoes, and a small black lacquered brush case hanging from the sash at the left hip.
The top of Kim Jongseo's head reaches Han Igyeom's mouth.
Han Igyeom wears the full dark lamellar armor coat over his black cheollik, helmet off, topknot visible, the same armor as in the previous scenes.
The top of Cheon Bongsu's head reaches only Han Igyeom's nose.
The top of Jo Yun's head reaches Han Igyeom's eyebrows.
The top of Cheon Bongsu's head reaches Jo Yun's eyes.
Kim Jongseo always stands on the left side of the courtyard near the open wooden gate, facing right with his left hand resting on his sheathed sword hilt and his face clearly lit under the brim of his black gat. Han Igyeom always stands or kneels in the center of the courtyard facing left toward Kim Jongseo, with the open grain storehouse behind him on the right. Cheon Bongsu and Jo Yun always kneel on the right side of the courtyard beside and slightly behind Han Igyeom. Two background cavalry banner-bearers halt at the gate on the far left with their faces small in profile. All faces have dry skin.

[Event Script]
0-4s: 50mm medium shot at eye level, camera locked off, framing the open wooden fortress gate on the left. Bright morning sunlight pours through the open gateway as Kim Jongseo walks into the courtyard on the left with his left hand resting on his sheathed sword hilt, while two cavalry banner-bearers halt behind him at the gate. All mouths closed.
4-8s: 50mm medium shot at eye level, camera locked off, framing Han Igyeom standing in the center holding the ledger, with Cheon Bongsu and Jo Yun on the right. Cheon Bongsu and Jo Yun drop onto one knee on the snow-dusted stone ground and bow their heads while Han Igyeom remains standing upright alone. At 5s, on-screen, Cheon Bongsu says (speaking in Korean, loud, firm and ringing, clear, crisp pronunciation), looking down toward the ground: "도절제사 영감, 뵙습니다!"
8-13s: 50mm medium two-shot at eye level, camera locked off, framing Kim Jongseo standing still on the left facing right and Han Igyeom standing in the center facing left so the top of Kim Jongseo's head reaches Han Igyeom's mouth. Standing alone among the kneeling officers, Han Igyeom bends ninety degrees from the waist in a polite modern office bow toward Kim Jongseo, then straightens up. At 9s, on-screen, Han Igyeom says (speaking in Korean, polite and welcoming like a middle-aged manager greeting a visiting executive, clear, crisp pronunciation): "먼 길 오시느라 고생 많으셨습니다."
13-18s: The key moment. Starting from a 50mm medium two-shot of Han Igyeom in the center and kneeling Cheon Bongsu on the right, the camera dollies in slowly to a medium close-up of Han Igyeom on his knee across this whole range; this is the only camera move in the clip. Keeping his head bowed, Cheon Bongsu reaches out his right hand, grips the lower hem of Han Igyeom's black cheollik robe, and pulls downward firmly; Han Igyeom flinches once and drops his right knee onto the stone ground with a dull thud, setting the ledger on the stone beside his left knee. Both mouths closed.
18-22s: 85mm medium close-up of Han Igyeom kneeling in the center, camera locked off. His brows draw together once, and he grips his sheathed sword hilt upright in front of his chest with both hands while looking down toward the left. Final frame: held on Han Igyeom kneeling with his brows drawn together slightly and both hands gripping his upright sword hilt in front of his chest, mouth closed.

[Visual and Camera Treatment]
All shots at eye level in the courtyard along a single action line, never crossing the 180-degree line: Kim Jongseo and the open gate always on the left, Han Igyeom always in the center, Cheon Bongsu, Jo Yun and the open grain storehouse always on the right. 50mm for medium shots and medium two-shots, 85mm for medium close-ups; size changes happen by cutting, not zooming. Camera locked off on a tripod in every shot except the single dolly-in at 13-18s; no zoom, no pan, no tilt, no other push-in, no drift, no handheld shake, no gimbal sway, no whip pan, no crane, no speed ramp. Speakers look at each other or bow toward the ground, never into the lens. Faces fill a large part of the frame in every shot, with morning light keeping Kim Jongseo's face clearly visible beneath the brim of his gat. Acting stays natural and restrained: small, realistic facial expressions and gestures, no exaggerated or comedic mugging. All Korean dialogue is pronounced clearly at a natural speaking pace, never mumbled or rushed. Lighting for this location: crisp, bright morning sunlight slants across the snow-covered fortress courtyard from the gate side on the left, casting clean shadows on the stone ground and illuminating the faces and wooden storehouse evenly.

[Audio]
No BGM; only ambient and action sounds: <firm leather boots stepping across snow-dusted stone at 0-3s>, <leather armor rustling as Cheon Bongsu and Jo Yun drop to one knee at 4s>, <heavy cloth tug followed by a dull thud of a knee hitting stone at 15s>, <metal scabbard clicking softly as Han Igyeom grips his upright sword hilt at 18s>. Cheon Bongsu speaks Korean in a loud, gruff, earnest voice of a stocky man in his forties. Han Igyeom speaks Korean in a deep young male voice, but with the hesitant, overly polite tone of a tired middle-aged office worker. Only the man speaking in each shot moves his mouth; the others keep their mouths closed.

[Maintain Consistency]
@Image 1 is Kim Jongseo, @Image 2 is Han Igyeom, @Image 3 is Cheon Bongsu, @Image 4 is Jo Yun, @Image 5 is the fortress gate courtyard. Keep all four men's faces, hairstyles, builds and clothing identical to their references, including Kim Jongseo's black horsehair gat with red tassel cord, deep crimson cheollik robe, brass-edged black leather lamellar vest and jade-buckled belt, Han Igyeom's topknot, neatly trimmed black beard, thin pale scar on the left eyebrow, black cheollik robe and dark brown studded leather lamellar vest, Cheon Bongsu's black horsehair headband (manggeon), short dense black mustache and brown leather lamellar armor, and Jo Yun's pale grey-blue silk dopo robe and dark navy chest sash. Keep Kim Jongseo on the left, Han Igyeom in the center, and Cheon Bongsu and Jo Yun kneeling on the right. Exactly six men (four named men and two background banner-bearers) are visible; no other person appears. Dry skin on all faces. Camera locked off except the one dolly-in. No BGM. Normal human eyes. Real-time natural speed, no slow motion. No subtitles, no on-screen text.
```

**속마음**

| 시점(초) | 화면 | 박만수 속마음 |
|---|---|---|
| 18–22초 | 돌바닥에 오른쪽 무릎을 꿇고 미간이 한 번 모인 한이겸 얼굴 (입 다묾) | "아우, 무릎이야." |

**효과음 자리**: 12초 "먼 길 오시느라 고생 많으셨습니다." 직후 [효과음: 띠용]

---

## 클립 07H — 성문 안 마당, 아침 (20초)

**참조**: 1 김종서 시트, 2 한이겸 시트, 3 천봉수 시트, 4 조윤 시트, 5 성문 안 마당 아침

```
[Generation Goal]
Live-action Korean historical comedy drama, real-time natural speed, 20 seconds (480 frames at 24 fps): one event — in the quiet fortress courtyard, Commander Kim Jongseo stops before the kneeling general, looks past his shoulder at the bare empty wall inside the open grain storehouse, asks how many sacks of grain remain, and the general raises his head and parts his lips to answer. Exactly four men are visible: Kim Jongseo, Han Igyeom, Cheon Bongsu, and Jo Yun. Eye-level camera, locked off except one dolly-in at 17-20s. No BGM.

[Reference Material Roles]
@Image 1 defines only Kim Jongseo's face, hairstyle, build and clothing. Do not copy its framing, grey background or panel layout. His facial expression comes from this shot description, not from @Image 1.
@Image 2 defines only Han Igyeom's face, hairstyle, build and clothing. Do not copy its framing, grey background or panel layout. His facial expression comes from this shot description, not from @Image 2.
@Image 3 defines only Cheon Bongsu's face, hairstyle, build and clothing. Do not copy its framing, grey background or panel layout. His facial expression comes from this shot description, not from @Image 3.
@Image 4 defines only Jo Yun's face, hairstyle, build and clothing. Do not copy its framing, grey background or panel layout. His facial expression comes from this shot description, not from @Image 4.
@Image 5 defines only the fortress gate courtyard's structures, ground and morning light: the wide-open wooden fortress gate on the left, the snow-covered stone courtyard in the center, and the open wooden grain storehouse on the right with a few low rows of straw sacks at the threshold and the bare empty wooden wall visible inside. @Image 5 is a style reference only, not a fixed keyframe.

[Subjects and Relationships]
Kim Jongseo corresponds to @Image 1: a dignified 51-year-old Korean military commander of the early Joseon dynasty, 172 cm, broad-shouldered and upright with a powerful, compact build, square, weathered face with a strong jaw and deep lines at the eyes and forehead, sharp, piercing dark eyes under thick black eyebrows streaked with grey, a calm, unsmiling mouth, a neatly trimmed black beard and mustache streaked with grey, black hair with grey at the temples tied in a topknot under a black horsehair gat with a red tassel cord, wearing a deep crimson cheollik commander's robe with a black leather lamellar vest edged in brass, a wide black belt with a jade-ornamented buckle, black leather boots, and a sheathed long sword at his left hip.
Han Igyeom corresponds to @Image 2: an original 28-year-old Korean man, 185 cm, broad-shouldered powerful warrior build with a thick chest and heavy muscular arms, short full black beard and mustache, neatly trimmed, a thin pale scar cuts vertically through the outer end of the left eyebrow, long black hair tied up in a traditional Joseon topknot, with a few loose strands falling beside the face, wearing a black heavy cotton cheollik military robe with a dark crimson inner lining showing at the collar, a dark brown leather lamellar vest with small iron studs over it, a wide black leather belt with a plain brass buckle, dark trousers tucked into black leather boots, and brown leather bracers on both forearms.
Cheon Bongsu corresponds to @Image 3: an original 45-year-old Korean man, 168 cm, short and stocky with a barrel chest, thick neck and strong short arms, round broad face with full ruddy sunburnt cheeks, a short dense black mustache and a sparse short goatee, short black hair tied in a small topknot, with a black woven horsehair headband (manggeon) across the forehead, wearing brown leather lamellar armor laced with dark cord over a dark grey cotton robe, a wide brown leather belt, dark grey trousers wrapped at the shins with off-white cloth leg bindings, and worn brown leather boots.
Jo Yun corresponds to @Image 4: an original 35-year-old Korean man, 176 cm, slender with an upright, composed posture, long narrow face with pale even skin and a few faint freckles across the bridge of the nose, narrow single-lidded dark eyes with a calm, unreadable gaze, thin lips set in a faint polite half-smile, a very thin, neatly trimmed mustache, black hair tied in a tidy topknot, wearing a pale grey-blue silk dopo scholar's robe with wide sleeves, a dark navy cord sash tied high at the chest, a white inner jacket collar visible at the neck, white beoseon socks, black taesahye shoes, and a small black lacquered brush case hanging from the sash at the left hip.
The top of Kim Jongseo's head reaches Han Igyeom's mouth.
Han Igyeom wears the full dark lamellar armor coat over his black cheollik, helmet off, topknot visible, the same armor as in the previous scenes.
The top of Cheon Bongsu's head reaches only Han Igyeom's nose.
The top of Jo Yun's head reaches Han Igyeom's eyebrows.
The top of Cheon Bongsu's head reaches Jo Yun's eyes.
Kim Jongseo always stands on the left side of the courtyard two paces in front of Han Igyeom, facing right with his left hand on his sword hilt and his face clearly illuminated under his black gat. Han Igyeom always kneels on his right knee in the center of the courtyard facing left toward Kim Jongseo, holding his sheathed sword upright in front of his chest with both hands, the closed paper ledger lying on the stone ground beside his left knee, and the open grain storehouse with its bare empty inner wall directly behind his shoulder on the right. Cheon Bongsu and Jo Yun always kneel on the right with their heads bowed. All faces have dry skin.

[Event Script]
0-3s: 50mm medium two-shot at eye level, camera locked off, framing Kim Jongseo on the left and kneeling Han Igyeom in the center with the open grain storehouse and its bare wooden inner wall visible over Han Igyeom's shoulder on the right. Kim Jongseo takes one step forward, stops two paces in front of Han Igyeom, and directs his steady gaze past Han Igyeom's shoulder toward the bare empty wall inside the open storehouse. Both mouths closed.
3-7s: 85mm medium close-up of Kim Jongseo standing on the left, camera locked off, his face clearly lit under his black gat, looking right past Han Igyeom toward the open storehouse, not at the lens. At 3.5s, on-screen, Kim Jongseo says (speaking in Korean, deep, calm and unhurried, clear, crisp pronunciation): "창고 문이 열려 있구나."
7-10s: 50mm medium shot at eye level, camera locked off, framing kneeling Han Igyeom in the center with the closed ledger beside his knee and kneeling Cheon Bongsu and Jo Yun on the right; Jo Yun lowers his bowed head slightly further toward the stone ground while Kim Jongseo on the left lowers his gaze from the ledger beside Han Igyeom's knee to Han Igyeom's face. All mouths closed.
10-14s: 85mm medium close-up of Han Igyeom kneeling in the center, camera locked off, both hands gripping his upright sword hilt, looking up left toward Kim Jongseo, not at the lens, as he blinks once. Mouth closed.
14-17s: 85mm medium close-up of Kim Jongseo standing on the left, camera locked off, his piercing dark eyes fixed down to the right on Han Igyeom, not at the lens. At 14s, on-screen, Kim Jongseo says (speaking in Korean, deep, calm and commanding, clear, crisp pronunciation): "군량이 몇 석이냐."
17-20s: The key moment. Starting from a 50mm medium close-up of Han Igyeom kneeling in the center, the camera dollies in slowly to an 85mm close-up of his face across this whole range; this is the only camera move in the clip. Han Igyeom shifts his grip on the upright sword hilt with both hands, raises his head toward Kim Jongseo on the left, and parts his lips slightly to speak without making a sound. Final frame: held on Han Igyeom's close-up face with his head raised and his lips slightly parted to answer, silent.

[Visual and Camera Treatment]
All shots at eye level in the courtyard along a single action line, never crossing the 180-degree line: Kim Jongseo always on the left, kneeling Han Igyeom always in the center, kneeling Cheon Bongsu and Jo Yun and the open grain storehouse always on the right. 50mm for medium shots and medium two-shots, 85mm for medium close-ups and close-ups; size changes happen by cutting, not zooming. Camera locked off on a tripod in every shot except the single dolly-in at 17-20s; no zoom, no pan, no tilt, no other push-in, no drift, no handheld shake, no gimbal sway, no whip pan, no crane, no speed ramp. Speakers look at each other, never into the lens. Faces fill a large part of the frame in every shot, with morning sunlight illuminating Kim Jongseo's face clearly under the brim of his gat. Acting stays natural and restrained: small, realistic facial expressions and gestures, no exaggerated or comedic mugging. All Korean dialogue is pronounced clearly at a natural speaking pace, never mumbled or rushed. Lighting for this location: crisp, bright morning sunlight slants across the snow-covered fortress courtyard from the gate side on the left, casting clean shadows on the stone ground and illuminating the faces and wooden storehouse evenly.

[Audio]
No BGM; only ambient and action sounds: <two firm boot steps stopping on stone at 0-2s>, <cold morning wind blowing quietly across the silent courtyard at 7-14s>, <leather gloves shifting on the upright sword hilt at 17s>. Kim Jongseo speaks Korean in a deep, calm, commanding voice of a man in his fifties, few words, never raised. Only the man speaking in each shot moves his mouth; the others keep their mouths closed.

[Maintain Consistency]
@Image 1 is Kim Jongseo, @Image 2 is Han Igyeom, @Image 3 is Cheon Bongsu, @Image 4 is Jo Yun, @Image 5 is the fortress gate courtyard. Keep all four men's faces, hairstyles, builds and clothing identical to their references, including Kim Jongseo's black horsehair gat with red tassel cord, deep crimson cheollik robe, brass-edged black leather lamellar vest and jade-buckled belt, Han Igyeom's topknot, neatly trimmed black beard, thin pale scar on the left eyebrow, black cheollik robe and dark brown studded leather lamellar vest, Cheon Bongsu's black horsehair headband (manggeon), short dense black mustache and brown leather lamellar armor, and Jo Yun's pale grey-blue silk dopo robe and dark navy chest sash. Keep Kim Jongseo standing on the left, Han Igyeom kneeling in the center with the ledger beside his knee and the open grain storehouse behind his shoulder on the right, and Cheon Bongsu and Jo Yun kneeling on the right. Exactly four men are visible; no other person appears. Dry skin on all faces. Camera locked off except the one dolly-in. No BGM. Normal human eyes. Real-time natural speed, no slow motion. No subtitles, no on-screen text.
```

**속마음**

| 시점(초) | 화면 | 박만수 속마음 |
|---|---|---|
| 10–14초 | 칼자루를 세워 쥐고 김종서를 올려다보는 한이겸 얼굴 클로즈업 (입 다묾) | "나랑 나이도 비슷해 보이는데… 눈빛이 상무님보다 무섭네." |

---

## 클립 08A — 거실, 아침 (24초)

**참조**: 1 박만수 시트, 2 정숙 시트, 3 거실 아침

```
[Generation Goal]
Live-action Korean comedy drama, real-time natural speed, 24 seconds (576 frames at 24 fps): one event — in a bright apartment living room in the morning, a fifty-four-year-old man wakes on the sofa still half in a Joseon dream, mumbles a grain count, is told off by his wife, sits up holding his lower back, and then has his right knee buckle once as he tries to stand, rubbing it with a tilted head. Exactly two people are visible: Park Mansu and Jeongsuk. Eye-level camera, locked off except one dolly-in at 20-24s. No BGM.

[Reference Material Roles]
@Image 1 defines only Park Mansu's face, hairstyle, build and clothing. Do not copy its framing, grey background or panel layout. His facial expression comes from this shot description, not from @Image 1.
@Image 2 defines only Jeongsuk's face, hairstyle, build and clothing. Do not copy its framing, grey background or panel layout. Her facial expression comes from this shot description, not from @Image 2.
@Image 3 defines only the apartment living room's furniture, walls and light in morning daylight: the beige fabric sofa with lace covers in the center-right, the sliding balcony window with flowered curtains behind the sofa on the right, the wooden dining table and chairs on the left, the round wall clock on the back wall between the white door and the window, and floral wallpaper. The dining table is bare and polished, with nothing on it. @Image 3 is a style reference only, not a fixed keyframe.

[Subjects and Relationships]
Park Mansu corresponds to @Image 1: an original 54-year-old Korean man, 175 cm, broad-shouldered sturdy build with thick forearms and a slight belly, short, thick, neatly trimmed salt-and-pepper hair, grey at the temples, combed back neatly, one small dark mole on the left cheekbone just below the left eye, wearing a charcoal grey zip-up padded work jacket in matte nylon over a navy blue polo shirt with the collar visible, dark grey slacks, worn black leather walking shoes, and a cheap silver wristwatch on the left wrist.
Jeongsuk corresponds to @Image 2: an original 52-year-old Korean woman, 162 cm, slim and well-kept figure, shoulder-length dark brown hair with soft loose waves, glossy and neatly styled with a side part, small pearl stud earrings, wearing a soft cream knit cardigan over a light blue and white striped cotton blouse, dark brown cotton trousers, grey house slippers, a navy blue apron printed with small white flowers tied at the waist, and a thin plain gold wedding ring.
The top of Jeongsuk's head reaches Park Mansu's nose.
Park Mansu is always on or beside the sofa on the right side of the frame. Jeongsuk always stands beside the bare dining table on the left side of the frame, holding a wooden rice paddle in her right hand. Both faces have dry skin.

[Event Script]
0-2s: 50mm medium shot at eye level, camera locked off. Park Mansu lies on his back on the sofa on the right, both hands gripping a black TV remote upright on his chest like a sword hilt. His eyes open once and look at the ceiling. Jeongsuk stands on the left beside the bare dining table, out of focus. Both mouths closed.
2-5s: 85mm medium close-up of Jeongsuk on the left beside the bare dining table, camera locked off, the wooden rice paddle in her right hand, looking right toward the sofa, not at the lens. At 2.5s, on-screen, she says (speaking in Korean at a natural pace, brisk and clear, clear, crisp pronunciation): "여보, 출근 안 해?"
5-9s: 85mm medium close-up of Park Mansu on the sofa on the right, camera locked off. He sets the remote down on the sofa, lifts both wrinkled hands in front of his face and turns the palms over once, then lowers his eyes and touches his belly with his right hand. At 7s, on-screen, he says (speaking in Korean in a low, hoarse, sleepy voice, slow with clear, crisp pronunciation), looking down at his hands: "백이십 석."
9-14s: 85mm medium close-up of Jeongsuk on the left beside the bare dining table, camera locked off. She puts her left hand on her hip, then points the rice paddle once toward the wall clock behind her. At 9s, on-screen, she says (speaking in Korean at a natural pace, a little louder, clear, crisp pronunciation, rising on the last words), looking right toward the sofa: "백이십 석 같은 소리 하고 있네. 일곱 시 반이야!"
14-17s: 50mm medium shot of Park Mansu on the sofa on the right, camera locked off. He swings his legs down to the floor, pushes himself up to sit on the sofa edge, and presses both hands to his lower back; his brows draw together once. At 15s, on-screen, he says (speaking in Korean as one short, low groan, clear, crisp pronunciation): "아이고."
17-20s: 85mm medium close-up of Park Mansu seated on the sofa edge on the right, camera locked off, both hands on his lower back, blinking once as he looks down at the floor while Jeongsuk on the left in the soft-focus background shakes her head once. Both mouths closed.
20-24s: The key moment. Starting from a 50mm medium shot of Park Mansu on the right side of the living room, the camera dollies in slowly to an 85mm medium close-up across this whole range; this is the only camera move in the clip. Park Mansu plants his feet on the floor and starts to rise from the sofa, his right knee buckles once making him pause half-risen, and he rubs his right knee over his dark grey slacks with his right hand while tilting his head once to the side. Final frame: held on Park Mansu rubbing his right knee over his slacks with his head tilted slightly to one side, both mouths closed.

[Visual and Camera Treatment]
All shots at eye level from the same side of the room, never crossing the 180-degree action line: Jeongsuk always on the left, Park Mansu always on the right. 50mm for medium shots, 85mm for medium close-ups; size changes happen by cutting, not zooming. Camera locked off on a tripod in every shot except the single dolly-in at 20-24s; no zoom, no pan, no tilt, no other push-in, no drift, no handheld shake, no gimbal sway, no whip pan, no crane, no speed ramp. Speakers look at each other, never into the lens. Faces fill a large part of the frame in every shot. Acting stays natural and restrained: small, realistic facial expressions and gestures, no exaggerated or comedic mugging. All Korean dialogue is pronounced clearly at a natural speaking pace, never mumbled or rushed. Lighting for this location: bright, clear morning daylight streams in through the sliding balcony window behind the sofa on the right, filling the living room with even natural light.

[Audio]
No BGM; only ambient and action sounds: <a smartphone alarm chiming briefly from the low table next to the sofa at 0-2s, then stopping>, <faint traffic far outside the balcony window on the right>, <sofa fabric rustling as Park Mansu sits up at 14-16s>, <trouser cloth rubbing softly as Park Mansu rubs his right knee at 21-23s>. Park Mansu speaks Korean in a warm, slightly husky baritone of a man in his fifties, speaking slowly and politely, groggy upon waking. Jeongsuk speaks Korean in a bright, brisk, warm voice of a woman in her forties. Only the person speaking in each shot moves their mouth; the other keeps their mouth closed.

[Maintain Consistency]
@Image 1 is Park Mansu, @Image 2 is Jeongsuk, @Image 3 is the apartment living room. Keep both faces, hairstyles, builds and clothing identical to their references, including Park Mansu's salt-and-pepper hair, small dark mole below the left eye, charcoal grey work jacket over navy polo shirt and cheap silver wristwatch on the left wrist, and Jeongsuk's shoulder-length wavy dark brown hair, pearl stud earrings, cream cardigan and navy blue apron with small white flowers. Keep the dining table bare, Jeongsuk on the left and Park Mansu on the sofa on the right. Exactly two people are visible; no other person appears. Dry skin on all faces. Camera locked off except the one dolly-in. No BGM. Normal human eyes. Real-time natural speed, no slow motion. No subtitles, no on-screen text.
```

**속마음**

| 시점(초) | 화면 | 박만수 속마음 |
|---|---|---|
| 17–20초 | 소파 끝에 앉아 두 손으로 허리를 짚고 바닥을 보는 박만수 얼굴 (입 다묾) | "꿈이었나." |

## 클립 08B — 현관, 아침 (12초)

**참조**: 1 박만수 경비복 시트, 2 하은 시트, 3 현관

**편집 메모**: 대본의 휴대폰 검색어 '쌀 한 섬 몇 킬로'는 시댄스가 글자를 망가뜨리므로 편집에서 휴대폰 화면 인서트(그래픽)로 0~2초 사이에 넣는다.

```
[Generation Goal]
Live-action Korean comedy drama, real-time natural speed, 12 seconds (288 frames at 24 fps): one event — in a narrow apartment entrance hall in the morning, a father in his security-guard uniform puts away his smartphone after looking up the weight of a sack of rice, tells his daughter he has eight hundred men to feed, and walks out to work. Exactly two people are visible: Park Mansu and Haeun. Eye-level camera, locked off except one dolly-in at 5-9s. No BGM.

[Reference Material Roles]
@Image 1 defines only Park Mansu's face, hairstyle, build and clothing. Do not copy its framing, grey background or panel layout. His facial expression comes from this shot description, not from @Image 1.
@Image 2 defines only Haeun's face, hairstyle, build and clothing. Do not copy its framing, grey background or panel layout. Her facial expression comes from this shot description, not from @Image 2.
@Image 3 defines only the apartment entrance hall's furniture, walls and light: the wooden shoe cabinet on the left, the tiled step-down entryway, and the closed metal front door on the right. @Image 3 is a style reference only, not a fixed keyframe.

[Subjects and Relationships]
Park Mansu corresponds to @Image 1: an original 54-year-old Korean man, 175 cm, broad-shouldered sturdy build with thick forearms and a slight belly, short, thick, neatly trimmed salt-and-pepper hair, grey at the temples, combed back neatly, one small dark mole on the left cheekbone just below the left eye, wearing a neat dark navy apartment security-guard uniform jacket buttoned over a light blue uniform shirt with a dark tie, matching dark navy guard trousers, black leather shoes, and a cheap silver wristwatch on the left wrist.
Haeun corresponds to @Image 2: an original 27-year-old Korean woman, 163 cm, slim build, dark brown double-lidded eyes with a flat, tired, indifferent look, faint dark circles under the eyes, one small dark mole just above the right side of the upper lip, long straight black hair worn loose with a center part, falling past the shoulders, wearing an oversized heather grey hoodie, black jogger pants, white canvas sneakers, and small silver stud earrings.
The top of Haeun's head reaches Park Mansu's nose.
Park Mansu always stands in the tiled entrance hall on the right side of the frame near the front exit, facing left toward Haeun until he walks out of frame to the right at 9s. Haeun always stands on the raised wooden hallway floor on the left side of the frame beside the shoe cabinet, facing right toward Park Mansu so the top of her head reaches his nose. Both faces have dry skin.

[Event Script]
0-2s: 50mm medium two-shot at eye level in the entrance hall, camera locked off, framing Haeun on the left beside the shoe cabinet and Park Mansu on the right in his dark navy security-guard uniform. Park Mansu finishes fastening the front button of his uniform jacket with his left hand while looking down at the smartphone held in his right hand; Haeun leans her head in slightly to glance down at his phone screen. Both mouths closed.
2-5s: 85mm medium close-up of Haeun standing on the left beside the shoe cabinet, camera locked off. She tilts her head slightly and raises her eyes from the phone screen to Park Mansu's face on the right, not at the lens. At 2s, on-screen, Haeun says (speaking in Korean at a natural pace, flat and even, clear, crisp pronunciation): "아빠, 그걸 왜 찾아?"
5-9s: The key moment. Starting from a 50mm medium close-up of Park Mansu on the right in his security-guard uniform, the camera dollies in slowly to an 85mm close-up across this whole range; this is the only camera move in the clip. Park Mansu slips the smartphone into his uniform jacket pocket with his right hand and looks left at Haeun, not at the lens, his jaw set. At 5.5s, on-screen, Park Mansu says (speaking in Korean, calm, low and earnest, clear, crisp pronunciation): "팔백 명을 먹여야 돼서."
9-12s: 85mm medium close-up of Haeun standing on the left beside the shoe cabinet, camera locked off. Park Mansu turns and walks out of frame past the right edge toward the front exit; a moment later, only the off-screen sound of the heavy metal front door opening and clicking shut is heard. Haeun stares at the right edge of the frame where he exited, her eyebrows lift once, she lets out one short breath through her nose, and the corner of her mouth twitches once. Final frame: held on Haeun staring at the right edge of the frame with her eyebrows still raised and lips pressed together, mouth closed.

[Visual and Camera Treatment]
All shots at standing eye level from the side of the entrance hall along a single action line, never crossing the 180-degree line: Haeun always on the left on the hallway floor, Park Mansu always on the right in the tiled entryway. 50mm for medium two-shots and medium close-ups, 85mm for close-ups; size changes happen by cutting, not zooming. Camera locked off on a tripod in every shot except the single dolly-in at 5-9s; no zoom, no pan, no tilt, no other push-in, no drift, no handheld shake, no gimbal sway, no whip pan, no crane, no speed ramp. Speakers look at each other, never into the lens. Faces fill a large part of the frame in every shot. Acting stays natural and restrained: small, realistic facial expressions and gestures, no exaggerated or comedic mugging. All Korean dialogue is pronounced clearly at a natural speaking pace, never mumbled or rushed. Lighting for this location: soft morning daylight from the living room behind joins the warm overhead entrance hall light, illuminating the front door and faces evenly.

[Audio]
No BGM; only ambient and action sounds: <smartphone screen tap at 0-1s>, <uniform cloth rustling as the phone slips into the pocket at 5s>, <leather shoes stepping out in the tiled entryway at 9-10s>, <heavy metal front door unlatching and closing with a solid click from just off-screen to the right at 10-11s>. Park Mansu speaks Korean in a warm, slightly husky baritone of a man in his fifties, speaking slowly and politely. Haeun speaks Korean in a low, flat, tired voice of a woman in her late twenties. Only the person speaking in each shot moves their mouth; the other keeps their mouth closed.

[Maintain Consistency]
@Image 1 is Park Mansu in his security-guard uniform, @Image 2 is Haeun, @Image 3 is the apartment entrance hall. Keep both faces, hairstyles, builds and clothing identical to their references, including Park Mansu's salt-and-pepper hair, small dark mole below the left eye, cheap silver wristwatch on the left wrist and dark navy security-guard uniform, and Haeun's center-parted long straight black hair, small dark mole above the right side of the upper lip, and oversized heather grey hoodie. Keep Haeun on the left beside the shoe cabinet and Park Mansu on the right in the entryway, with the front door heard off-screen at the end. Exactly two people are visible; no other person appears. Dry skin on all faces. Camera locked off except the one dolly-in. No BGM. Normal human eyes. Real-time natural speed, no slow motion. No subtitles, no on-screen text.
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
| 거실 (식탁·소파, 밤) | `docs/locations/living_room.png` (GPT, ChatGPT 구독) | media `d41bfb3a-186f-4f03-9b19-9ebca8d5e2bc` |
| 김종서 시트 | `docs/sheets/kimjongseo.png` (GPT) | media `67392243-f9fd-46c1-bb3a-85af14b2be85` |
| 성문 안 마당 (아침) | `docs/locations/gate_courtyard_morning.png` (GPT) | media `6cbd87b2-f77b-4226-bddb-78acf52cb6dc` |
| 거실 아침 | `docs/locations/living_room_morning.png` (GPT) | media `5b86f75a-81e1-410d-b9d3-9d44b1640d9c` |
