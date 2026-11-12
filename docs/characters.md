# 인물 설정집

character-consistency 스킬의 Character Brief 형식. 각 인물의 **IDENTITY** 블록은 이미지·영상 프롬프트에 글자 그대로 붙여 넣는다.

모든 인물은 창작 인물이다. 실존 인물이나 배우를 닮게 만들지 않는다.

## 키 관계

키 숫자(cm)는 모델이 잘 안 지킨다. 두 사람이 한 화면에 나오는 컷에는 **"누구 머리 꼭대기가 누구의 어디에 닿는다"**는 문장을 프롬프트에 같이 넣는다. 아래 문장은 키 차이로 계산한 것이라 실제와 맞는다.

| 조합 | 키 | 프롬프트에 넣을 문장 |
|---|---|---|
| 한이겸 / 천봉수 | 185 / 168 | `The top of Cheon Bongsu's head reaches only Han Igyeom's nose.` |
| 한이겸 / 조윤 | 185 / 176 | `The top of Jo Yun's head reaches Han Igyeom's eyebrows.` |
| 조윤 / 천봉수 | 176 / 168 | `The top of Cheon Bongsu's head reaches Jo Yun's eyes.` |
| 박만수 / 정숙 | 175 / 162 | `The top of Jeongsuk's head reaches Park Mansu's nose.` |
| 박만수 / 하은 | 175 / 163 | `The top of Haeun's head reaches Park Mansu's nose.` |
| 정숙 / 하은 | 162 / 163 | `Jeongsuk and Haeun are about the same height.` |

한이겸과 천봉수의 키 차이(17cm)는 개그에 쓴다. 천봉수가 한이겸을 올려다보며 말하는 구도가 기본이다.

---

## 고정 목소리 (일레븐랩스 eleven_v4, 대사 소리 참조용)

| 인물 | 목소리 | voice_id | 상태 |
|---|---|---|---|
| 박만수(현대·속마음) | 박만수 후보1 | `xikVJWJpydm4MXCV89Y2` | 확정 |
| 천봉수 | Deok - Energetic Korean Narrator | `wisKdlUQEBMjkKqNAa3c` | 확정 (정면 립싱크 테스트 통과) |
| 군관1(마른 30대) | Kyung Hoon - Calm & Natural | `JsyP5NIpAZhfPw5mwSP0` | 사용 중 |
| 한이겸·조윤·군관2·정숙·하은·관리소장·최 상무·김종서 | — | — | 미정 |

## 박만수 (현대)

- **확정 시트**: `docs/sheets/parkmansu.png` (힉스필드 job `98e0a6a0-cb83-4572-8339-67c05035e377`). 기준 얼굴 job `57e4fe0c-9bcc-4f95-8a49-28543487c4b7`.

- **나이/체격**: 54세 한국 남성, 175cm. 어깨가 넓고 팔뚝이 굵은 떡대, 배가 살짝 나왔다. 듬직하고 호감 가는 옆집 아저씨 인상.
- **알아보는 표시**: 왼쪽 눈 아래 광대 위의 작은 점, 왼손목의 싸구려 은색 시계.
- **기본 표정**: 지쳤지만 순하고 따뜻한 눈, 입가에 옅은 미소.
- **목소리 (속마음·현대 장면 공통)**: 일레븐랩스 `박만수 후보1` (voice_id `xikVJWJpydm4MXCV89Y2`), 모델 `eleven_v4`. 지시 태그는 `[talking to himself at a normal speaking volume, ...]`처럼 **평소 음량**으로. 속삭임·중얼거림 태그는 쓰지 않는다.
- **의상(시즌 1 기본)**: 진회색 작업 점퍼, 남색 폴로셔츠, 진회색 슬랙스, 낡은 검정 구두.

**IDENTITY**
```
Park Mansu, an original 54-year-old Korean man, 175 cm, broad-shouldered sturdy build with thick forearms and a slight belly, a dependable and likable dad-next-door look. Square face with a firm jaw, healthy warm tan complexion, smile lines at the eyes and mouth, gentle crow's feet. Kind, warm dark brown eyes, slightly tired, with naturally muted catchlights. Thick dark eyebrows with a few grey hairs. Straight sturdy nose, full lips with a faint good-natured closed-mouth smile at rest. Clean-shaven with a light shadow on the jaw. One small dark mole on the left cheekbone just below the left eye. Natural skin with visible pores and fine wrinkles. Short, thick, neatly trimmed salt-and-pepper hair, grey at the temples, combed back neatly. Wearing a charcoal grey zip-up padded work jacket in matte nylon, worn and slightly frayed at the cuffs, over a navy blue polo shirt with the collar visible, dark grey slacks, worn black leather walking shoes, and a cheap silver wristwatch on the left wrist.
```

## 한이겸 (조선, 속은 박만수)

- **확정 시트**: `docs/sheets/hanigyeom.png` (힉스필드 job `63cb6e08-d28c-4664-af11-533a329286cb`). 기준 얼굴 job `3eb17134-4008-4149-a495-ac50af59281b`.

- **나이/체격**: 28세 한국 남성, 185cm. 어깨가 넓고 가슴이 두꺼운 무인 체격.
- **알아보는 표시**: 왼쪽 눈썹을 가로지르는 옅은 흉터, 상투에서 흘러내린 잔머리.
- **기본 표정**: 침착하고 굳은 얼굴. 박만수가 들어간 뒤에는 눈빛이 순해진다.
- **의상(시즌 1 기본)**: 검은 철릭, 짙은 갈색 가죽 찰갑 조끼, 가죽 팔토시, 검은 장화.
- **말투 단계** (조선에서의 박만수):
  1. **1~2화, 현대어**: 부하에게 "실례지만 어디서 오셨어요?", "회의부터 합시다". 고쳐 보려다 "누구시, 누구시오, 누구냐"처럼 버벅인다. 부하들은 "어찌 존대를 하십니까", "말에서 떨어지셨다던데" 하며 수군댄다.
  2. **3~5화, 어설픈 사극체**: 사극에서 들은 말투를 흉내 내다 틀린다. "~하거라요", "짐이"처럼 왕 말투가 섞여 부하들이 기겁한다. 회사 말("결재 올려", "보고서", "파이팅")은 계속 튀어나와 부하들이 군령인 줄 알고 받아 적는다.
  3. **6화 이후, 하오체 정착**: 조선 말투가 자연스러워진다. 대신 **현대에서 사극 말투가 튀어나온다**("이놈, 분리수거를 이리 하면 되겠느냐"). 말투가 어느 쪽에서 튀는지가 두 세계 비중의 지표가 된다.

**IDENTITY**
```
Han Igyeom, an original 28-year-old Korean man, 185 cm, broad-shouldered powerful warrior build with a thick chest and heavy muscular arms. Mature angular face with a strong defined jaw and high cheekbones, adult bone structure. Short full black beard and mustache, neatly trimmed. Straight nose with a slight bump on the bridge. Deep-set dark brown double-lidded eyes with an intense steady gaze and naturally muted catchlights. Thick straight black eyebrows; a thin pale scar cuts vertically through the outer end of the left eyebrow. Sun-tanned skin with visible pores and fine texture. Long black hair tied up in a traditional Joseon topknot, with a few loose strands falling beside the face. Wearing a black heavy cotton cheollik military robe with a dark crimson inner lining showing at the collar, a dark brown leather lamellar vest with small iron studs over it, a wide black leather belt with a plain brass buckle, dark trousers tucked into black leather boots, and brown leather bracers on both forearms.
```

## 천봉수 (조선)

- **확정 시트**: `docs/sheets/cheonbongsu.png` (힉스필드 job `52fad13a-8e00-49bf-881b-0bdaa5e32315`). 기준 얼굴 job `992d8cc4-7806-4bd0-a44d-f7c6d9054867`.

- **나이/체격**: 45세 한국 남성, 168cm. 키는 작고 통이 굵은 땅딸막한 체격.
- **알아보는 표시**: 짧고 숱 많은 콧수염, 붉게 탄 둥근 볼, 이마의 검은 망건.
- **기본 표정**: 눈을 동그랗게 뜬 성실한 얼굴.
- **의상**: 갈색 가죽 찰갑, 짙은 회색 무명 두루마기, 가죽 띠, 각반.

**IDENTITY**
```
Cheon Bongsu, an original 45-year-old Korean man, 168 cm, short and stocky with a barrel chest, thick neck and strong short arms. Round broad face with full ruddy sunburnt cheeks, small round dark brown eyes with an earnest wide-eyed look and naturally muted catchlights, short thick black eyebrows, a flat broad nose, a short dense black mustache and a sparse short goatee. Weathered skin with visible pores and fine lines at the eyes. Short black hair tied in a small topknot, with a black woven horsehair headband (manggeon) across the forehead. Wearing brown leather lamellar armor laced with dark cord over a dark grey cotton robe, a wide brown leather belt, dark grey trousers wrapped at the shins with off-white cloth leg bindings, and worn brown leather boots.
```

## 조윤 (조선, 종사관)

- **확정 시트**: `docs/sheets/joyun.png` (힉스필드 job `24c87eb6-9680-424b-bfc6-a206ecaf1c76`). 기준 얼굴 job `3c620fb8-0220-4acc-83af-cefdffac78fc`.

- **나이/체격**: 35세 한국 남성, 176cm. 마르고 곧은 자세.
- **알아보는 표시**: 콧등의 옅은 주근깨, 허리에 찬 작은 붓 통.
- **기본 표정**: 속을 알 수 없는 옅은 미소.
- **의상**: 옅은 청회색 비단 도포, 남색 세조대, 흰 버선, 검은 태사혜.

**IDENTITY**
```
Jo Yun, an original 35-year-old Korean man, 176 cm, slender with an upright, composed posture. Long narrow face with mature adult structure, pale even skin with fine natural texture and a few faint freckles across the bridge of the nose. Narrow single-lidded dark eyes with a calm, unreadable gaze and naturally muted catchlights, thin neatly arched black eyebrows, a straight thin nose, thin lips set in a faint polite half-smile. Clean-shaven except for a very thin, neatly trimmed mustache. Black hair tied in a tidy topknot with no loose strands. Wearing a pale grey-blue silk dopo scholar's robe with wide sleeves, a dark navy cord sash tied high at the chest, a white inner jacket collar visible at the neck, white beoseon socks, black taesahye shoes, and a small black lacquered brush case hanging from the sash at the left hip.
```

## 정숙 (현대, 아내)

- **확정 시트**: `docs/sheets/jeongsuk.png` (힉스필드 job `b843e5a5-b920-4b9a-b473-9515449371f1`). 기준 얼굴 job `9c2688c3-ff14-46cf-b8fd-add61520aa8f`.

- **나이/체격**: 52세 한국 여성, 162cm. 날씬하고 관리 잘한 미시 스타일. 40대 초중반으로 보인다.
- **알아보는 표시**: 남색 바탕에 작은 흰 꽃무늬 앞치마, 어깨 길이 웨이브 머리, 진주 귀걸이.
- **기본 표정**: 생기 있고 다정한 미소.
- **의상**: 크림색 니트 가디건, 하늘색 줄무늬 블라우스, 갈색 면바지, 앞치마.

**IDENTITY**
```
Jeongsuk, an original 52-year-old Korean woman, 162 cm, slim and well-kept figure, an elegant and pretty young-looking mother who reads as early-to-mid forties. Soft oval face with defined cheekbones and a gentle jawline, mature adult features. Clear bright skin with natural fine texture and faint smile lines at the eyes. Large warm dark brown double-lidded eyes with naturally muted catchlights, softly shaped natural eyebrows. Light natural makeup: thin brown eyeliner, rosy coral lip color, faint blush. Shoulder-length dark brown hair with soft loose waves, glossy and neatly styled with a side part, a few strands tucked behind the right ear. Small pearl stud earrings. Wearing a soft cream knit cardigan over a light blue and white striped cotton blouse, dark brown cotton trousers, grey house slippers, a navy blue apron printed with small white flowers tied at the waist, and a thin plain gold wedding ring.
```

## 하은 (현대, 딸)

- **확정 시트**: `docs/sheets/haeun.png` (힉스필드 job `4260d24f-e8ae-43d9-8bbe-cfb1ea3341c9`). 기준 얼굴 job `4c46c5f4-4f20-4fe6-835a-37c2ed3e4bdc`.

- **나이/체격**: 27세 한국 여성, 163cm. 마른 체격.
- **알아보는 표시**: 오른쪽 윗입술 위의 작은 점, 가운데 가르마의 긴 생머리.
- **기본 표정**: 무심하고 지친 얼굴, 옅은 다크서클.
- **의상**: 오버사이즈 회색 후드티, 검은 조거 팬츠, 흰 운동화, 작은 은색 귀걸이.

**IDENTITY**
```
Haeun, an original 27-year-old Korean woman, 163 cm, slim build. Oval face with mature adult bone structure, a defined jawline and cheekbones, not a babyface. Dark brown double-lidded eyes with a flat, tired, indifferent look, faint dark circles under the eyes, naturally muted catchlights. Natural straight dark eyebrows. One small dark mole just above the right side of the upper lip. Matte skin with visible fine texture and minimal makeup. Long straight black hair worn loose with a center part, falling past the shoulders. Wearing an oversized heather grey hoodie, black jogger pants, white canvas sneakers, and small silver stud earrings.
```

---

## 최 상무 (현대, 박만수의 옛 부하)

- **확정 시트**: `docs/sheets/choi.png` (힉스필드 job `059450e6-1190-4951-8559-641bb0c48d51`).
- **나이/체격**: 48세 한국 남성, 178cm. 마르고 단정함.
- **알아보는 표시**: 무테안경, 날카로운 옆 가르마.
- **목소리**: `a polished, smooth, businesslike voice of a man in his late forties`

**IDENTITY**
```
Executive Choi, an original 48-year-old Korean man, 178 cm, slim and well-groomed. Narrow oval face with a smooth jaw, clean-shaven, light even skin with fine natural texture. Thin rimless glasses over calm dark brown eyes, neat straight eyebrows. Short black hair with a sharp side part, neatly gelled. Wearing a fitted charcoal navy suit, a white shirt, a muted dark blue silk tie, black leather oxford shoes and a slim silver wristwatch.
```

## 관리소장 (현대)

- **확정 시트**: `docs/sheets/manager.png` (힉스필드 job `694d2811-b832-4af3-883a-55d6ad5c4c90`).
- **나이/체격**: 63세 한국 남성, 168cm. 마르고 등이 약간 굽음.
- **알아보는 표시**: 코끝에 걸친 검은 뿔테 돋보기, 남색 누빔 조끼의 이름표.
- **목소리**: `a dry, slow, raspy voice of a man in his sixties`

**IDENTITY**
```
The Office Manager, an original 63-year-old Korean man, 168 cm, thin and slightly stooped. Long weathered face with deep forehead wrinkles and hollow cheeks, grey stubble. Small tired dark eyes, bushy grey eyebrows, thick black-framed reading glasses resting low on his nose. Thinning grey hair combed over to one side. Wearing a navy blue quilted work vest with a small name tag over a beige checked flannel shirt, grey work trousers and worn brown slip-on shoes.
```

## 김종서 (조선, 실존 인물 · 2화부터)

- **확정 시트**: 아직 없음. 2화 생성 전에 만든다.
- **위치**: 함길도 도절제사. 한이겸의 직속 상관. 별명 대호(大虎).
- **나이/체격**: 51세. 키는 한이겸보다 작지만(약 172cm) 어깨가 넓고 꼿꼿하다. 실존 초상이 없으므로 위엄 있는 50대 무장으로 새로 만든다.
- **표현 원칙**: 개그의 대상이 되지 않는다. 품위와 위엄을 지킨다. 웃음은 그를 대하는 박만수와 군관들 쪽에서 나온다.
- **목소리**: `a deep, calm, commanding voice of a man in his fifties, few words, never raised`
- **키 문장**: `The top of Kim Jongseo's head reaches Han Igyeom's mouth.` (172 / 185)

**IDENTITY**
```
Kim Jongseo, a dignified 51-year-old Korean military commander of the early Joseon dynasty, 172 cm, broad-shouldered and upright with a powerful, compact build. Square, weathered face with a strong jaw and deep lines at the eyes and forehead. Sharp, piercing dark eyes under thick black eyebrows streaked with grey, a calm, unsmiling mouth. A neatly trimmed black beard and mustache streaked with grey. Black hair with grey at the temples tied in a topknot under a black horsehair gat with a red tassel cord. Wearing a deep crimson cheollik commander's robe with a black leather lamellar vest edged in brass, a wide black belt with a jade-ornamented buckle, black leather boots, and a sheathed long sword at his left hip.
```
