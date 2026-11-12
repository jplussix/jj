# 1화 클립 목록과 프롬프트

- 모델: 시댄스 2.5 (힉스필드 `seedance_2_5`, `omni_reference`), 480p, 16:9, 소리 생성 켬
- 규칙: 한 클립 = 한 장소, 끊기지 않는 시간. 30초 이하. 대사는 클립당 6~8줄 이하.
- 자막("세종 16년…", "열여덟 시간 전")은 영상에 넣지 않고 편집에서 넣는다.
- `@Image N`은 참조 이미지를 넣는 순서다. 각 클립의 **참조** 목록 순서대로 넣는다.
- 클립 5-A는 `clip05a.md`에 따로 있다 (테이크 1 채택 후보).

## 클립 목록

| 클립 | 씬 | 장소 | 길이 | 등장 | 상태 |
|---|---|---|---|---|---|
| 01 | 1 | 성루, 밤 | 25초 | 한이겸, 천봉수, 군관들 | 프롬프트 완료 |
| 02A | 2 | 물류센터 사무실 | 25초 | 박만수, 최 상무 | 프롬프트 완료 |
| 02B | 2 | 물류센터 창고 | 15초 | 박만수, 지게차 기사 | 프롬프트 완료 |
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

## 클립 02A — 물류센터 사무실 (25초)

**참조**: 1 박만수 시트, 2 최 상무 시트, 3 물류센터 사무실

```
[Generation Goal]
A quiet, sad office scene: a veteran warehouse manager is laid off by his former subordinate and signs the paper.

[Reference Material Roles]
@Image 1 defines Park Mansu's face, hairstyle, build and clothing. Do not use the grey background or the panel layout.
@Image 2 defines Executive Choi's face, hairstyle, build and clothing. Do not use the grey background or the panel layout.
@Image 3 defines the small glass-walled office overlooking the warehouse floor. @Image 3 is a style reference only, not a fixed keyframe.

[Subjects and Relationships]
Park Mansu corresponds to @Image 1; Executive Choi corresponds to @Image 2. They sit facing each other across a desk; Park Mansu on the left, Executive Choi on the right. On the desk lie one sheet of paper and a ballpoint pen. Through the glass wall behind them, forklifts move across the warehouse floor.

[Event Script]
Stage 1 - The offer: Park Mansu stares down at the paper. Executive Choi says softly in Korean, {부장님, 저도 마음이 안 좋습니다.} Park Mansu looks up and says in Korean, {상무님. 우리 애 취직할 때까지만요. 일 년만.} End state: Executive Choi lowers his eyes.
Stage 2 - The pen: Executive Choi says in Korean, {본사 결재가 어제 끝났어요.} Park Mansu picks up the pen, puts it down, picks it up again. He says quietly in Korean, {제가 여기서 이십칠 년입니다.} Executive Choi answers in Korean, {그래서 위로금도 넉넉히 넣었습니다.} End state: Park Mansu holds the pen over the paper.
Stage 3 - The signature: Park Mansu signs. He lifts a locker key on a lanyard from around his neck and lays it on the paper. End state: hold on the key resting on the signed paper.

[Visual and Camera Treatment]
Stage 1 is a two-shot across the desk at eye level. Stage 2 alternates over-the-shoulder shots. Stage 3 is a close-up of the hands, the pen and the key. Flat cool fluorescent office light; daylight from the warehouse behind the glass.

[Audio]
<muffled forklift beeps from the warehouse>, <a ticking wall clock>. Park Mansu speaks Korean in a warm, slightly husky baritone of a man in his fifties, speaking slowly and politely. Executive Choi speaks Korean in a polished, smooth, businesslike voice of a man in his late forties.

[Maintain Consistency]
Keep both faces and clothing identical to their references; keep Park Mansu on the left and Executive Choi on the right of the desk throughout.
```

## 클립 02B — 물류센터 창고 (15초)

**참조**: 1 박만수 시트, 2 물류센터 창고

```
[Generation Goal]
A short bittersweet moment: on his way out with his belongings, a laid-off warehouse manager still corrects a forklift driver.

[Reference Material Roles]
@Image 1 defines Park Mansu's face, hairstyle, build and clothing. Do not use the grey background or the panel layout.
@Image 2 defines the warehouse aisles, numbered loading lanes and racks. @Image 2 is a style reference only, not a fixed keyframe.

[Subjects and Relationships]
Park Mansu corresponds to @Image 1 and carries a cardboard box of personal belongings in both arms. A young forklift driver in a yellow safety vest and helmet sits in a forklift ahead of him, about to lower a pallet in the middle of the aisle. A large painted number 3 marks the lane on the floor.

[Event Script]
Stage 1 - Leaving: Park Mansu walks down the aisle with the box. The forklift begins lowering its pallet into the aisle. Seeing it, Park Mansu stops. End state: he faces the forklift.
Stage 2 - One last order: Park Mansu calls out in Korean, {어이, 거기 내리면 삼 번 라인 막혀. 오 번 뒤로 빼.} The driver startles and answers in Korean, {아, 네! 부장님!} and reverses the forklift. Park Mansu watches until it has fully turned away, then walks on toward the exit door. End state: hold on his back as he reaches the door.

[Visual and Camera Treatment]
Medium shot tracking backward in front of Park Mansu, then a reverse shot of the forklift, then a medium-wide shot from behind him walking to the bright exit door. High warehouse lighting, daylight spilling from the open door.

[Audio]
<forklift engine and reverse beeping>, <footsteps on concrete>. Park Mansu speaks Korean in a warm, slightly husky baritone of a man in his fifties, raising his voice firmly. The driver speaks Korean in a young, startled male voice.

[Maintain Consistency]
Keep Park Mansu's face and clothing identical to @Image 1 and the box in his arms throughout.
```

## 클립 03 — 관리사무소 (30초)

**참조**: 1 박만수 시트, 2 관리소장 시트, 3 관리사무소

```
[Generation Goal]
A dry comic job interview: a laid-off manager in his fifties applies to be an apartment security guard.

[Reference Material Roles]
@Image 1 defines Park Mansu's face, hairstyle, build and clothing. Do not use the grey background or the panel layout.
@Image 2 defines the Office Manager's face, hairstyle, build and clothing. Do not use the grey background or the panel layout.
@Image 3 defines the cramped apartment management office with a duty roster on the wall and a window. @Image 3 is a style reference only, not a fixed keyframe.

[Subjects and Relationships]
Park Mansu corresponds to @Image 1; the Office Manager corresponds to @Image 2 and wears reading glasses low on his nose. The Office Manager sits behind a cluttered desk holding a résumé; Park Mansu sits upright on a folding chair across from him, both hands on his knees. The window behind the desk looks out on a recycling area piled high with cardboard boxes.

[Event Script]
Stage 1 - Age: The Office Manager reads over his glasses and says in Korean, {쉰넷. 나이가 좀 많으시네.} Park Mansu answers in Korean, {체력은 자신 있습니다.} End state: the Office Manager keeps reading.
Stage 2 - Experience: The Office Manager says in Korean, {물류센터 부장을 하셨네. 경비 일은 해 보셨어요?} Park Mansu says in Korean, {아니요.} The Office Manager asks in Korean, {그럼 특기가 뭡니까?} Park Mansu answers with full seriousness in Korean, {재고 조사입니다.} End state: the Office Manager slowly lowers his glasses and looks at him.
Stage 3 - Hired: The Office Manager repeats flatly in Korean, {재고 조사.} Park Mansu says earnestly in Korean, {숫자하고 물건이 안 맞으면 잠이 안 옵니다.} The Office Manager points out the window at the mountain of boxes and says in Korean, {저거나 좀 맞춰 봐요. 내일부터 야간입니다.} Park Mansu stands and bows deeply from the waist. End state: hold on the deep bow.

[Visual and Camera Treatment]
Mostly a static two-shot from the side of the desk at eye level, cutting to a close-up of the Office Manager lowering his glasses in Stage 2 and to the window view of the boxes in Stage 3. Warm afternoon window light, a dim fluorescent tube overhead.

[Audio]
<a small desk fan humming>, <paper rustling>. Park Mansu speaks Korean in a warm, slightly husky baritone of a man in his fifties, speaking slowly and politely. The Office Manager speaks Korean in a dry, slow, raspy voice of a man in his sixties.

[Maintain Consistency]
Keep both faces and clothing identical to their references; keep the Office Manager behind the desk and Park Mansu on the chair throughout.
```

## 클립 04 — 거실, 밤 (30초)

**참조**: 1 박만수 시트, 2 정숙 시트, 3 하은 시트, 4 거실

```
[Generation Goal]
A quiet family dinner where a father fails to tell his family he lost his job, then falls asleep in front of a period drama on TV.

[Reference Material Roles]
@Image 1 defines Park Mansu's face, hairstyle, build and clothing. Do not use the grey background or the panel layout.
@Image 2 defines Jeongsuk's face, hairstyle, build and clothing. Do not use the grey background or the panel layout.
@Image 3 defines Haeun's face, hairstyle, build and clothing. Do not use the grey background or the panel layout.
@Image 4 defines the apartment's dining table, living room sofa and TV. @Image 4 is a style reference only, not a fixed keyframe.

[Subjects and Relationships]
Park Mansu corresponds to @Image 1, Jeongsuk to @Image 2, Haeun to @Image 3. At the dining table, Park Mansu sits at the head, Jeongsuk on his left pasting receipts into a household ledger, Haeun on his right eating while looking at her phone. A pot of doenjang stew sits in the middle of the table.

[Event Script]
Stage 1 - Trying: Park Mansu holds his spoon and looks between them. He says hesitantly in Korean, {저기, 내가 할 말이.} Without looking up, Jeongsuk says in Korean, {여보, 이번 달 대출 이자 또 올랐어.} Park Mansu closes his mouth. End state: he turns to Haeun.
Stage 2 - Haeun: Park Mansu asks in Korean, {하은아, 면접은.} Haeun says flatly in Korean, {아빠는 몰라도 돼.} She takes her bowl and walks off to her room; a door closes off-screen. End state: the chair on his right is empty.
Stage 3 - Nothing: Jeongsuk asks in Korean, {회사는 별일 없지?} Park Mansu takes a spoonful of stew and says in Korean, {별일 없지.} End state: he chews slowly, eyes down.
Stage 4 - The TV: Later, Park Mansu sits alone on the sofa holding the remote. On the TV screen, an actor dressed as a Joseon general draws a sword and shouts in Korean, {전군, 나를 따르라!} Park Mansu's head slowly droops; he begins to snore. End state: hold on him asleep with the remote in his hand and the TV light on his face.

[Visual and Camera Treatment]
Stages 1 to 3 are a static medium shot of the table from the far end, with a close-up of Park Mansu for his last line. Stage 4 cuts to a medium shot of the sofa from beside the TV. Warm pendant light over the table; in Stage 4 the room is dark except the flickering blue TV light.

[Audio]
<spoons on bowls>, <a door closing>, <TV period drama music>. Park Mansu speaks Korean in a warm, slightly husky baritone of a man in his fifties, speaking slowly and politely. Jeongsuk speaks Korean in a bright, brisk, warm voice of a woman in her forties. Haeun speaks Korean in a low, flat, tired voice of a woman in her late twenties. The TV actor shouts in a booming theatrical male voice.

[Maintain Consistency]
Keep all three faces and clothing identical to their references; keep Jeongsuk on Park Mansu's left and Haeun on his right at the table.
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
