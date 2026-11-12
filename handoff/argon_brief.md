# 조선만수록 — 대본·프롬프트 작성 설명서 (아르곤용)

이 파일 하나에 작품 설정, 인물 고정 문구, 1화 대본, 출력 형식이 전부 들어 있다. **이 규격을 그대로 지켜** 2화 대본(`scripts/ep02.md`)과 2화 클립 프롬프트(`storyboard/ep02/clips.md`)를 작성한다.

---

## 0. 작업 흐름

1. 아르곤이 이 설명서대로 `ep02.md`와 `clips.md` **두 파일의 전문**을 출력한다. 각 파일은 맨 위에 `=== FILE: scripts/ep02.md ===`, `=== FILE: storyboard/ep02/clips.md ===` 한 줄을 붙여 구분한다.
2. 사용자가 그 출력을 그대로 Claude에게 붙여 넣는다.
3. Claude가 저장소에 저장하고, 규격 검수(인물 문구, 길이, 대사량, 참조)를 한 뒤 참조 이미지를 붙여 영상과 소리를 생성한다.

아르곤은 이미지나 영상을 만들지 않는다. **글만 쓴다.** 참조 이미지 ID(job 번호)도 Claude가 채운다. 아르곤은 참조 목록에 이름만 적는다.

---

## 1. 작품 개요

- **제목**: 조선만수록(朝鮮萬壽錄). 매 화 콜드오픈 뒤에 6초 타이틀이 붙는다(이미 제작됨).
- **한 줄**: 명예퇴직 당한 54세 가장 박만수가 잠들 때마다 세종 16년(1434) 함길도 변방 삭풍진의 28세 장군 한이겸의 몸으로 깨어난다.
- **규칙**: 잠들면 조선, 깨면 현대. 하룻밤이 조선의 하루. 물건은 못 가져가고 지식만 가져간다. 조선에서 익힌 담력과 버릇은 현대의 몸에 조금씩 남는다.
- **타깃**: 50~60대 시청자. 약간 유치해도 되지만 웃음과 감동이 둘 다 있어야 한다. 주성치식으로 진지해서 웃긴 개그.
- **레퍼런스**: 유튜브 씬나루 〈장군님 출근하십니다〉의 구조(현대와 과거 교차, 능력 과시와 참교육, 담담한 감동, 한 칸씩 오르는 로맨스나 관계 사다리). 단, 설정 장치(포털, 현대 알바, 물건 운반)는 쓰지 않는다.

## 2. 매 화 구조 (지킬 것)

1. **조선의 문제** (성벽, 군량, 역병, 적, 내부 첩자)
2. **낮의 공부**: 현대에서 박만수가 그 문제의 해결책을 찾는다(유튜브, 철물점 사장, 한의사 친구, 예비역 동창 등)
3. **현대의 사건**: 갑질 입주민, 보이스피싱, 일진 등. 장군 버릇이 튀어나와 참교육
4. **밤의 적용**: 배운 것으로 조선의 문제를 푼다. 부하들이 놀란다
5. **훅**: 잠에서 깨는 순간, 또는 위기 직전에 끊는다

## 3. 유머 코드

- **진지한 오해**: 주인공은 웃기려 하지 않는다. 진지해서 웃기다.
- **회사 말투가 조선에서 튀어나옴**: "회의부터 합시다", "결재 올려", "본사 감사".
- **말투 단계**: 1~2화는 현대어 존댓말로 버벅임 → 3~5화는 어설픈 사극체(왕 말투가 섞여 부하들이 기겁) → 6화 이후는 하오체가 정착하고 거꾸로 현대에서 사극체가 튀어나옴. **2화는 아직 1단계 후반이다.** 조금씩 "~소", "~하시오"를 흉내 내기 시작하는 정도.
- **키 개그**: 천봉수(168cm)가 한이겸(185cm)을 올려다보며 말한다.
- **박만수 속마음**: 조선 장면에서 한이겸 얼굴 위로 50대 아저씨 목소리 속마음이 한마디씩 깔린다. 상황 설명 겸 개그.

## 4. 감동 코드

- 눈물을 짜지 않는다. 담담한 선의가 쌓인다.
- 현대: 가족에게 퇴직 사실을 숨긴 아버지. 딸과 아내가 아버지가 달라진 걸 조금씩 알아본다.
- 조선: 장군이 달라졌다며 따르는 병사와 백성. 김종서와 박만수는 나이가 비슷하다(51세, 54세). 박만수만 아는 동질감.
- 시즌 줄기: 박만수는 김종서가 19년 뒤 계유정난(1453)에서 죽는다는 걸 안다. 2화에서는 아직 꺼내지 않는다. 복선 한 줄 정도만 허용.

## 5. 실존 인물 원칙

- 주인공 한이겸과 삭풍진 부대는 **가상**이다. 실존 인물(세종, 김종서)은 옆에서 등장한다.
- 김종서는 개그의 대상이 아니다. 품위를 지킨다.
- 실제 사건의 날짜와 결과는 바꾸지 않는다.
- 전설·야사를 쓰면 화 끝 자막으로 밝힌다.

## 6. 2화에서 꼭 들어갈 것

- **오프닝**: 1화 끝 직후. 김종서(대호)가 삭풍진에 도착, 군량 창고를 둘러본다. 백팔십 석이 빈 사실을 한이겸이 어떻게 "보고"하는가. 박만수는 회사에서 본부장에게 하던 대로 보고한다(결론부터, 원인, 대책).
- **김종서의 반응**: 처음엔 이상하게 보지만, 장부를 맞추는 꼼꼼함에 관심을 보인다. 조윤은 긴장한다.
- **현대 파트**: 박만수의 아파트 경비 첫 야간 근무. 1화에서 빠진 **현대 참교육**을 넣는다(예: 경비를 하대하는 갑질 입주민). 장군 버릇이 튀어나와 통쾌하게 정리. 가족 쪽 감동 한 장면.
- **다음 화 훅** 하나.
- 2화 콜드오픈 → 타이틀 → 본편 순서. 콜드오픈은 30초 이하 한 클립.

---

## 7. 대본 형식 (`scripts/ep02.md`)

1화 대본(부록 C)과 **같은 형식**으로 쓴다.

- 맨 위: 제목 `# 조선만수록 — 2화 「부제」`, 분량, 화면비, 말투 메모
- `## 등장인물` 표, `## 장면 배분` 표(씬, 장소, 길이)
- 씬마다 `## 씬 N. 장소 — 시간`
- 지문은 **카메라에 보이는 것만** 쓴다. 속마음을 지문으로 설명하지 않는다.
- 대사는 `**인물명**` 다음 줄에 대사.
- **속마음 표기**: `**박만수(속마음)**` 다음 줄에 대사. 조선 장면에서만 쓴다. 한 씬에 1~3줄.
- **자막**: `**자막**` 다음 줄에 내용.
- **효과음 자리**: 개그 포인트에 `[효과음: 정적]`, `[효과음: 띠용]`처럼 지문 줄로 표시. 한 씬에 0~2개.
- 분량 목표: 7~9분. 대사는 분당 240자 안팎. 대사 한 줄은 짧게(25자 안팎).

## 8. 클립 형식 (`storyboard/ep02/clips.md`)

1화 클립 파일과 같은 형식이다. 예시는 부록 D.

### 클립 나누기 규칙

- **한 클립 = 한 장소, 끊기지 않는 시간.** 씬 경계를 넘지 않는다.
- **30초 이하.** 대사는 클립당 6~8줄 이하. 너무 많으면 입이 따라가지 못한다.
- 클립 번호는 씬 번호 + 알파벳(01, 02A, 02B…).
- 한 화면에 이름 있는 인물은 2~4명까지. 군관, 병사, 입주민 같은 단역은 시트 없이 묘사로만 처리하고 얼굴이 크게 나오지 않게 둔다.
- **아주 멀리서 잡아 얼굴이 작게 나오는 컷은 피한다**(480p로 뽑아 업스케일하기 때문). 풀숏, 와이드숏 자체는 괜찮다.

### 파일 구조

1. `## 클립 목록` 표: 클립 | 씬 | 장소 | 길이 | 등장 | 상태
2. `## 생성 전에 만들어야 할 참조 이미지` 표: 새로 필요한 인물 시트, 의상 시트, 장소
3. 클립마다:
   - `## 클립 NN — 장소 (길이)`
   - `**참조**: 1 인물명 시트, 2 인물명 시트, 3 장소명` (이름만. ID는 Claude가 채움)
   - 프롬프트 코드블록 (아래 7칸 구조, **영어**, 대사만 한국어)
   - `**속마음**` 표: 시점(초) | 화면 | 박만수 속마음 (조선 클립에만, 없으면 생략)
   - `**효과음 자리**`: 있으면 한 줄로

### 프롬프트 7칸 구조 (순서 고정, 영어)

```
[Generation Goal]
한두 문장: 영상 종류, 중심 인물, 핵심 사건.

[Reference Material Roles]
참조 하나에 한 줄씩. 인물: "@Image N defines <Name>'s face, hairstyle, build and clothing. Do not use the grey background or the panel layout."
장소: "@Image N defines <장소 설명>. @Image N is a style reference only, not a fixed keyframe."

[Subjects and Relationships]
각 인물을 참조에 연결하고, 고정된 물건(문, 탁자, 성벽) 기준으로 위치를 쓴다. 두 사람이 같이 나오면 부록 B의 키 문장을 넣는다.

[Event Script]
Stage 1 - 이름: Opening state: ... 한 가지 주요 행동 ... End state: 보이는 상태.
Stage 2 - 이름: ... (한 단계에 주요 변화 하나. 반응보다 원인을 먼저 쓴다. 마지막 단계는 멈춘 상태로 끝낸다.)
대사는 {중괄호 안에 한국어}로, 누가 어떻게 말하는지 영어로 앞에 쓴다. 예: Cheon Bongsu says in Korean, {장군, 명을 내리소서.}

[Visual and Camera Treatment]
샷 크기 + 움직임 + 방향 + 대상. 빛은 실제 광원과 방향. "dramatic", "dynamic" 같은 형용사만 쓰지 않는다.

[Audio]
<효과음>은 꺾쇠, 대사는 위 Event Script의 중괄호. 말하는 인물마다 부록 A의 **목소리 문구를 글자 그대로** 쓴다.
속마음은 여기 넣지 않는다(편집에서 따로 얹음).

[Maintain Consistency]
한 문장: 바뀌면 안 되는 것(얼굴, 의상, 위치 관계, 카메라 쪽).
```

### 프롬프트 금지 사항

- 부록 A의 인물 외형을 **다시 묘사하지 않는다.** 참조 이미지가 얼굴과 옷을 정한다. 프롬프트에는 이름과 참조 연결만 쓴다(갑옷이나 투구처럼 시트와 다른 소품을 추가할 때만 그 소품을 쓴다).
- 부정문 금지("no sword" 대신 "both hands empty").
- 카메라에 안 보이는 것을 쓰지 않는다. 화면 밖 사건은 소리나 빛으로만.
- 길이, 화면비, 해상도를 프롬프트 안에 쓰지 않는다(생성 설정으로 들어감).
- 대본에 없는 대사를 지어내지 않는다.

---

## 부록 A. 인물 설정 (외형 고정 문구, 키 문장 = 부록 B 포함)

각 인물의 IDENTITY 블록은 Claude가 이미지 생성에 쓰는 원본이다. 아르곤은 이 내용을 **읽고 인물을 이해하는 데만** 쓰고, 클립 프롬프트에 외형을 다시 묘사하지 않는다. job 번호와 voice_id는 Claude용이니 무시한다.

### 시댄스 목소리 문구 (클립 [Audio]에 글자 그대로)

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
| 김종서 | `a deep, calm, commanding voice of a man in his fifties, few words, never raised` |

### 인물 설정집

character-consistency 스킬의 Character Brief 형식. 각 인물의 **IDENTITY** 블록은 이미지·영상 프롬프트에 글자 그대로 붙여 넣는다.

모든 인물은 창작 인물이다. 실존 인물이나 배우를 닮게 만들지 않는다.

#### 키 관계

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

#### 박만수 (현대)

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

#### 한이겸 (조선, 속은 박만수)

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

#### 천봉수 (조선)

- **확정 시트**: `docs/sheets/cheonbongsu.png` (힉스필드 job `52fad13a-8e00-49bf-881b-0bdaa5e32315`). 기준 얼굴 job `992d8cc4-7806-4bd0-a44d-f7c6d9054867`.

- **나이/체격**: 45세 한국 남성, 168cm. 키는 작고 통이 굵은 땅딸막한 체격.
- **알아보는 표시**: 짧고 숱 많은 콧수염, 붉게 탄 둥근 볼, 이마의 검은 망건.
- **기본 표정**: 눈을 동그랗게 뜬 성실한 얼굴.
- **의상**: 갈색 가죽 찰갑, 짙은 회색 무명 두루마기, 가죽 띠, 각반.

**IDENTITY**
```
Cheon Bongsu, an original 45-year-old Korean man, 168 cm, short and stocky with a barrel chest, thick neck and strong short arms. Round broad face with full ruddy sunburnt cheeks, small round dark brown eyes with an earnest wide-eyed look and naturally muted catchlights, short thick black eyebrows, a flat broad nose, a short dense black mustache and a sparse short goatee. Weathered skin with visible pores and fine lines at the eyes. Short black hair tied in a small topknot, with a black woven horsehair headband (manggeon) across the forehead. Wearing brown leather lamellar armor laced with dark cord over a dark grey cotton robe, a wide brown leather belt, dark grey trousers wrapped at the shins with off-white cloth leg bindings, and worn brown leather boots.
```

#### 조윤 (조선, 종사관)

- **확정 시트**: `docs/sheets/joyun.png` (힉스필드 job `24c87eb6-9680-424b-bfc6-a206ecaf1c76`). 기준 얼굴 job `3c620fb8-0220-4acc-83af-cefdffac78fc`.

- **나이/체격**: 35세 한국 남성, 176cm. 마르고 곧은 자세.
- **알아보는 표시**: 콧등의 옅은 주근깨, 허리에 찬 작은 붓 통.
- **기본 표정**: 속을 알 수 없는 옅은 미소.
- **의상**: 옅은 청회색 비단 도포, 남색 세조대, 흰 버선, 검은 태사혜.

**IDENTITY**
```
Jo Yun, an original 35-year-old Korean man, 176 cm, slender with an upright, composed posture. Long narrow face with mature adult structure, pale even skin with fine natural texture and a few faint freckles across the bridge of the nose. Narrow single-lidded dark eyes with a calm, unreadable gaze and naturally muted catchlights, thin neatly arched black eyebrows, a straight thin nose, thin lips set in a faint polite half-smile. Clean-shaven except for a very thin, neatly trimmed mustache. Black hair tied in a tidy topknot with no loose strands. Wearing a pale grey-blue silk dopo scholar's robe with wide sleeves, a dark navy cord sash tied high at the chest, a white inner jacket collar visible at the neck, white beoseon socks, black taesahye shoes, and a small black lacquered brush case hanging from the sash at the left hip.
```

#### 정숙 (현대, 아내)

- **확정 시트**: `docs/sheets/jeongsuk.png` (힉스필드 job `b843e5a5-b920-4b9a-b473-9515449371f1`). 기준 얼굴 job `9c2688c3-ff14-46cf-b8fd-add61520aa8f`.

- **나이/체격**: 52세 한국 여성, 162cm. 날씬하고 관리 잘한 미시 스타일. 40대 초중반으로 보인다.
- **알아보는 표시**: 남색 바탕에 작은 흰 꽃무늬 앞치마, 어깨 길이 웨이브 머리, 진주 귀걸이.
- **기본 표정**: 생기 있고 다정한 미소.
- **의상**: 크림색 니트 가디건, 하늘색 줄무늬 블라우스, 갈색 면바지, 앞치마.

**IDENTITY**
```
Jeongsuk, an original 52-year-old Korean woman, 162 cm, slim and well-kept figure, an elegant and pretty young-looking mother who reads as early-to-mid forties. Soft oval face with defined cheekbones and a gentle jawline, mature adult features. Clear bright skin with natural fine texture and faint smile lines at the eyes. Large warm dark brown double-lidded eyes with naturally muted catchlights, softly shaped natural eyebrows. Light natural makeup: thin brown eyeliner, rosy coral lip color, faint blush. Shoulder-length dark brown hair with soft loose waves, glossy and neatly styled with a side part, a few strands tucked behind the right ear. Small pearl stud earrings. Wearing a soft cream knit cardigan over a light blue and white striped cotton blouse, dark brown cotton trousers, grey house slippers, a navy blue apron printed with small white flowers tied at the waist, and a thin plain gold wedding ring.
```

#### 하은 (현대, 딸)

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

#### 최 상무 (현대, 박만수의 옛 부하)

- **확정 시트**: `docs/sheets/choi.png` (힉스필드 job `059450e6-1190-4951-8559-641bb0c48d51`).
- **나이/체격**: 48세 한국 남성, 178cm. 마르고 단정함.
- **알아보는 표시**: 무테안경, 날카로운 옆 가르마.
- **목소리**: `a polished, smooth, businesslike voice of a man in his late forties`

**IDENTITY**
```
Executive Choi, an original 48-year-old Korean man, 178 cm, slim and well-groomed. Narrow oval face with a smooth jaw, clean-shaven, light even skin with fine natural texture. Thin rimless glasses over calm dark brown eyes, neat straight eyebrows. Short black hair with a sharp side part, neatly gelled. Wearing a fitted charcoal navy suit, a white shirt, a muted dark blue silk tie, black leather oxford shoes and a slim silver wristwatch.
```

#### 관리소장 (현대)

- **확정 시트**: `docs/sheets/manager.png` (힉스필드 job `694d2811-b832-4af3-883a-55d6ad5c4c90`).
- **나이/체격**: 63세 한국 남성, 168cm. 마르고 등이 약간 굽음.
- **알아보는 표시**: 코끝에 걸친 검은 뿔테 돋보기, 남색 누빔 조끼의 이름표.
- **목소리**: `a dry, slow, raspy voice of a man in his sixties`

**IDENTITY**
```
The Office Manager, an original 63-year-old Korean man, 168 cm, thin and slightly stooped. Long weathered face with deep forehead wrinkles and hollow cheeks, grey stubble. Small tired dark eyes, bushy grey eyebrows, thick black-framed reading glasses resting low on his nose. Thinning grey hair combed over to one side. Wearing a navy blue quilted work vest with a small name tag over a beige checked flannel shirt, grey work trousers and worn brown slip-on shoes.
```

#### 김종서 (조선, 실존 인물 · 2화부터)

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


---

## 부록 B. 키 문장

부록 A 맨 위 '키 관계' 표, 그리고 김종서 항목의 키 문장을 쓴다.

---

## 부록 C. 1화 대본 (형식과 톤의 기준)

### 조선만수록 — 1화 「일단 회의부터 합시다」

- 분량: 약 6분 40초 / 대사 약 970자 (65줄)
- 속마음 표기: `**박만수(속마음)**` (일레븐랩스로 만들어 편집에서 얹음, 입 안 움직임)
- 화면비: 16:9
- 말투: 현대 인물은 해요체, 조선 군관은 합쇼체. 조선에서의 박만수는 1화에서 현대어 존댓말을 쓰다가 사극 말투를 흉내 내려고 버벅인다. 화가 갈수록 하오체에 적응한다 (`docs/characters.md`의 말투 단계 참고)

#### 등장인물

| 이름 | 세계 | 외형 | 비고 |
|---|---|---|---|
| 박만수 | 현대 | 54세. 듬직한 떡대, 순한 인상, 희끗한 짧은 머리. 회색 점퍼 | 물류센터 관리부장 27년 |
| 한이겸 | 조선 | 28세. 근육질, 수염, 상투. 검은 철릭에 갑옷 | 삭풍진 병마첨절제사. 김종서 휘하. 속은 박만수 |
| 천봉수 | 조선 | 40대. 땅딸막한 떡대, 둥근 얼굴, 가죽 갑옷 | 군관. 충직하고 눈치가 느림 |
| 조윤 | 조선 | 30대. 마르고 흰 얼굴, 단정한 도포 | 종사관. 장부 담당 |
| 정숙 | 현대 | 52세. 단발, 앞치마 | 아내 |
| 하은 | 현대 | 27세. 긴 머리, 후드티 | 딸. 취업 준비 중 |
| 최 상무 | 현대 | 48세. 날씬한 정장, 무테 안경 | 박만수의 옛 부하 |
| 관리소장 | 현대 | 60대. 조끼, 돋보기 | 아파트 관리소장 |

#### 장면 배분

| 씬 | 장소 | 길이 |
|---|---|---|
| 1 | 삭풍진 성루, 밤 | 0:40 |
| 2 | 물류센터 사무실, 낮 | 1:00 |
| 3 | 아파트 관리사무소, 낮 | 0:50 |
| 4 | 박만수의 집 거실, 밤 | 0:50 |
| 5 | 삭풍진 군막, 새벽 | 1:10 |
| 6 | 삭풍진 성루와 군막, 아침 | 1:10 |
| 7 | 삭풍진 군량 창고, 아침 | 0:40 |
| 8 | 박만수의 집 거실, 아침 | 0:20 |

---

#### 씬 1. 삭풍진 성루 — 밤

눈발이 날린다. 성벽 너머 들판에 횃불 수천 개가 깔려 있다.

**자막**
세종 16년(1434), 함길도 북방 삭풍진

갑옷을 입은 한이겸이 성가퀴를 두 손으로 붙잡고 서 있다. 손가락이 떨린다.

**박만수(속마음)**
여기 어디야. 웬 불이 저렇게 많아.

천봉수가 한쪽 무릎을 꿇는다. 뒤로 군관 여섯이 따라 꿇는다.

**천봉수**
적이 육천입니다. 아군은 팔백입니다.

**박만수(속마음)**
육천? 팔백? …재고 얘긴가.

한이겸이 침을 삼킨다.

**천봉수**
장군, 명을 내리소서.

한이겸이 입을 연다. 소리가 나오지 않는다.

**박만수(속마음)**
장군? 나한테 하는 소리야?

화면이 꺼진다.

**자막**
열여덟 시간 전

---

#### 씬 2. 물류센터 사무실 — 낮

유리벽 너머로 지게차가 오간다. 책상 위에 서류 한 장과 볼펜.

박만수가 서류를 내려다본다. 맞은편에 최 상무가 앉아 있다.

**최 상무**
부장님, 저도 마음이 안 좋습니다.

**박만수**
상무님. 우리 애 취직할 때까지만요. 일 년만.

**최 상무**
본사 결재가 어제 끝났어요.

박만수가 볼펜을 든다. 내려놓는다. 다시 든다.

**박만수**
제가 여기서 이십칠 년입니다.

**최 상무**
그래서 위로금도 넉넉히 넣었습니다.

박만수가 서명한다. 목에 건 사물함 열쇠를 벗어 서류 위에 올려놓는다.

박만수가 종이 상자를 안고 창고를 가로질러 걷는다. 지게차 한 대가 통로에 팔레트를 내려놓으려 한다.

박만수가 걸음을 멈춘다.

**박만수**
어이, 거기 내리면 삼 번 라인 막혀. 오 번 뒤로 빼.

**지게차 기사**
아, 네! 부장님!

지게차가 방향을 바꾼다. 박만수가 그걸 끝까지 지켜보고 나서야 문을 나선다.

---

#### 씬 3. 아파트 관리사무소 — 낮

좁은 사무실. 벽에 경비 근무표. 관리소장이 돋보기 너머로 이력서를 본다.

박만수가 작업 점퍼 차림 그대로 무릎에 손을 얹고 앉아 있다.

**관리소장**
쉰넷. 나이가 좀 많으시네.

**박만수**
체력은 자신 있습니다.

**관리소장**
물류센터 부장을 하셨네. 경비 일은 해 보셨어요?

**박만수**
아니요.

**관리소장**
그럼 특기가 뭡니까?

**박만수**
재고 조사입니다.

관리소장이 돋보기를 내린다.

**관리소장**
재고 조사.

**박만수**
숫자하고 물건이 안 맞으면 잠이 안 옵니다.

관리소장이 창밖을 가리킨다. 재활용장에 상자가 산처럼 쌓여 있다.

**관리소장**
저거나 좀 맞춰 봐요. 내일부터 야간입니다.

박만수가 일어나 허리를 깊이 숙인다.

---

#### 씬 4. 박만수의 집 거실 — 밤

식탁에 된장찌개. 정숙이 가계부에 영수증을 붙인다. 하은은 밥을 먹으며 휴대폰을 본다.

박만수가 숟가락을 든 채 두 사람을 번갈아 본다.

**박만수**
저기, 내가 할 말이.

**정숙**
여보, 이번 달 대출 이자 또 올랐어.

박만수가 입을 다문다.

**박만수**
하은아, 면접은.

**하은**
아빠는 몰라도 돼.

하은이 그릇을 들고 방으로 들어간다. 문이 닫힌다.

**정숙**
회사는 별일 없지?

박만수가 찌개를 한 숟갈 뜬다.

**박만수**
별일 없지.

거실 소파. 텔레비전에서 사극이 나온다. 장수가 칼을 뽑으며 외친다.

**텔레비전 속 장수**
전군, 나를 따르라!

박만수가 리모컨을 쥔 채 고개를 떨군다. 코를 곤다.

---

#### 씬 5. 삭풍진 군막 — 새벽

북소리.

한이겸이 눈을 뜬다. 천장이 천막이다. 벌떡 일어나 앉는다.

**한이겸**
아이고.

한이겸이 멈춘다. 허리를 만진다. 무릎을 굽혔다 편다.

**한이겸**
안 아프네.

자기 손을 본다. 주름이 없다. 굵은 팔뚝을 쥐어 본다. 배를 더듬는다. 납작하다.

놋대야의 물에 얼굴을 비춘다. 수염 난 젊은 얼굴.

**한이겸**
누구세요.

물속의 얼굴이 같은 입 모양을 한다.

천봉수가 군막 자락을 걷고 들어온다.

**천봉수**
장군, 기침하셨습니까.

한이겸이 대야를 등 뒤로 감춘다.

**한이겸**
저, 실례지만 어디서 오셨어요?

천봉수가 그 자리에 굳는다.

**천봉수**
장군, 어찌 소인한테 존대를 하십니까?

**한이겸**
아, 그러니까. 그대는, 누구시, 누구시오. 누구냐.

한이겸이 말할 때마다 천봉수의 눈이 커진다.

**천봉수**
군관 천봉수입니다. 십 년을 모셨습니다.

천봉수가 한이겸의 이마에 손등을 댄다.

**천봉수**
열은 없으신데, 말씀이 영 이상하십니다.

밖에서 북소리가 빨라진다.

**천봉수**
적이 진을 쳤습니다. 성루로 가셔야 합니다.

천봉수가 투구를 내민다. 한이겸이 그걸 받아 거꾸로 쓴다. 천봉수가 말없이 돌려 씌운다.

---

#### 씬 6. 삭풍진 성루와 군막 — 아침

씬 1의 자리. 날이 밝았다. 들판에 적의 천막이 끝없이 이어진다.

**천봉수**
적이 육천입니다. 아군은 팔백입니다. 장군, 명을 내리소서.

군관 여섯이 한이겸을 올려다본다. 조윤은 한 걸음 뒤에 서서 소매에 손을 넣고 있다.

한이겸이 성가퀴를 붙잡는다. 군관들을 본다. 들판을 본다. 다시 군관들을 본다.

**한이겸**
일단 회의부터 합시다.

군관들이 서로 쳐다본다.

**천봉수**
장군, 저희한테 '합시다'라니요.

**천봉수**
그리고 회의가 무엇입니까?

**한이겸**
다 같이 앉아서 얘기하는 거예요. 거요. 거다.

군막. 군관들이 긴 탁자에 둘러앉았다. 다들 어색하게 허리를 편다.

군관 둘이 고개를 붙이고 속삭인다.

**군관1**
장군 말씀이 왜 저러시나.

**군관2**
어젯밤에 말에서 떨어지셨다던데.

한이겸이 그쪽을 본다. 둘이 동시에 허리를 편다.

**한이겸**
먼저 현황부터. 쌀이 얼마나 남았소?

**조윤**
삼백 석입니다. 넉 달은 버팁니다.

**한이겸**
장부 좀 봅시다.

조윤이 잠깐 멈췄다가 장부를 내민다. 한이겸이 장을 넘긴다. 손가락으로 줄을 따라 내려간다. 한 줄에서 멈춘다.

**한이겸**
지난달에 이백 석이 들어왔는데, 나간 건 오십 석이네.

**조윤**
그렇습니다.

**한이겸**
그 전에 남은 게 백오십 석. 합치면 삼백 석. 숫자는 맞소.

조윤의 어깨가 내려간다.

**한이겸**
그런데 받은 사람 수결이 석 달째 한 사람 글씨요.

조윤이 소매 속에서 손을 쥔다.

**한이겸**
입고하는 사람하고 확인하는 사람이 같으면 안 되지. 창고 갑시다.

**천봉수**
지금 말입니까? 적이 코앞인데.

**한이겸**
그러니까 지금 세야지.

---

#### 씬 7. 삭풍진 군량 창고 — 아침

어두운 창고. 쌀섬이 벽을 따라 쌓여 있다. 겉에서 보면 가득 차 보인다.

**한이겸**
한 줄에 열 섬씩. 줄 맞춰 다시 쌓으시오.

병사들이 섬을 옮긴다. 앞줄을 들어내자 뒤쪽이 텅 비어 있다. 병사들이 웅성거린다.

섬이 열 개씩 줄지어 놓인다. 천봉수가 손가락으로 줄을 센다.

**천봉수**
열, 열하나, 열둘. 열두 줄입니다.

**한이겸**
백이십 석.

천봉수가 붓을 들어 장부의 '삼백' 위에 줄을 긋고 옆에 '일백이십'이라 쓴다.

**천봉수**
백여든 석이 빕니다.

군관들이 일제히 조윤을 본다. 조윤은 표정이 없다.

**조윤**
쥐가 들었나 봅니다.

**한이겸**
쥐가 백여든 석을 먹으면 소만 해졌겠소.

병사 하나가 웃음을 터뜨리다 입을 막는다.

조윤이 한이겸에게 한 걸음 다가선다. 목소리를 낮춘다.

**조윤**
장군께서 언제부터 셈에 그리 밝으셨습니까.

한이겸의 관자놀이에 땀이 맺힌다.

밖에서 뿔나팔 소리.

**병사(소리)**
기병이다! 성문으로 온다!

군관들이 칼자루를 쥔다. 잠시 뒤.

**병사(소리)**
아니다! 우리 깃발이다! 도절제사 영감이시다!

군관들의 얼굴이 하얘진다. 천봉수가 한이겸에게 바짝 붙는다.

**천봉수**
장군, 대호(大虎)께서 오셨습니다. 하필 오늘.

한이겸이 텅 빈 창고 안쪽을 돌아본다. 눈을 질끈 감는다.

**한이겸**
본사 감사가 왜 하필 지금.

---

#### 씬 8. 박만수의 집 거실 — 아침

휴대폰 알람.

박만수가 소파에서 눈을 뜬다. 리모컨을 칼처럼 두 손으로 쥐고 있다.

**정숙**
여보, 출근 안 해?

박만수가 자기 손을 본다. 주름진 손. 배를 만진다. 나와 있다.

**박만수**
백이십 석.

**정숙**
백이십 석 같은 소리 하고 있네. 일곱 시 반이야!

박만수가 일어난다.

**박만수**
아이고.

허리를 짚는다. 이번에는 진짜로 아프다.

현관. 박만수가 경비복 단추를 채우며 휴대폰에 글자를 친다. 화면에 검색어가 보인다. '쌀 한 섬 몇 킬로'.

하은이 방에서 나오다 화면을 본다.

**하은**
아빠, 그걸 왜 찾아?

박만수가 휴대폰을 주머니에 넣는다.

**박만수**
팔백 명을 먹여야 돼서.

박만수가 문을 열고 나간다. 하은이 닫힌 문을 본다.

**끝.**


---

## 부록 D. 1화 클립 예시 (클립 형식의 기준)

### 클립 05B — 군막 (30초)

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

---

## 부록 E. 세계관

### 세계관 — 시즌 1: 김종서의 북방

#### 시대

- **세종 16년(1434)**, 함길도(지금의 함경도) 북방.
- 세종이 두만강 유역에 여섯 진(6진: 종성, 온성, 회령, 경원, 경흥, 부령)을 세우던 시기다. 김종서는 이 무렵 함길도 도절제사로 북방 개척을 지휘했다.
- 적은 두만강 일대의 **여진** 부족들. 실록에는 '오랑캐(兀良哈, 올량합)'가 특정 여진 부족 이름으로도 나온다. 그래서 대사의 "오랑캐"는 시대에 맞는 말이다.

#### 가상과 실제의 경계

| 가상 | 실제 |
|---|---|
| 삭풍진 (6진 사이의 작은 진), 한이겸, 천봉수, 조윤, 적 육천 대 아군 팔백 | 세종, 김종서, 6진 개척, 함길도, 여진과의 대치 |

- **주인공과 그 부대는 가상이다.** 실존 인물은 옆에서 등장한다. 개그는 가상 인물이 맡고, 실존 인물(특히 김종서)은 품위를 지킨다.
- 실제 사건의 날짜와 결과는 바꾸지 않는다. 박만수가 바꾸는 건 삭풍진 안의 일뿐이다.
- 전설이나 야사를 쓸 때는 화 끝에 자막으로 밝힌다.

#### 김종서 (실존 인물)

- **위치**: 함길도 도절제사. 한이겸의 직속 상관.
- **별명**: 대호(大虎, 큰 호랑이). 군관들이 이 이름만 들어도 굳는다.
- **역할**: 박만수에게는 "무서운 본사 본부장". 박만수는 회사에서 하던 대로 결재판을 들고 보고하러 가는데, 이게 김종서 눈에는 이상하게 꼼꼼한 장수로 보인다. 처음엔 의심하다 점점 아끼게 된다.
- **나이**: 1383년생이라 1434년에 51세 전후. 박만수(54세)와 비슷한 나이다. 박만수만 그걸 느끼는 데서 오는 묘한 동질감이 감동 줄기가 된다.
- **외형**: 남아 있는 확실한 초상이 없다. 위엄 있는 50대 무장으로 새로 만든다. (캐릭터 시트 아직 없음)

#### 시즌을 끌고 가는 줄기

- 박만수는 역사책으로 **김종서가 19년 뒤 계유정난(1453)에서 죽는다**는 걸 안다.
- 말해 줄 수도, 모른 척할 수도 없다. 이 갈등이 시즌 후반의 감동 줄기다.
- 역사는 바꾸지 않는다. 대신 박만수는 김종서에게 "살아남는 법"이 아니라 무언가 다른 것을 남긴다. (결말은 시즌 중반에 정한다)

#### 1화와의 연결

- 1화 끝: 텅 빈 군량 창고를 발견한 바로 그때 김종서가 순찰을 온다. 박만수: "본사 감사가 왜 하필 지금."
- 2화 시작: 김종서 앞에서 박만수가 군량 장부 문제를 어떻게 보고하는가.

#### 시즌 2 후보 (메모)

- 권율과 행주산성(임진왜란). 정숙의 앞치마에서 착안해 박만수가 부녀자들에게 치마로 돌을 나르게 하고, 이것이 '행주치마'가 됐다는 개그. 행주치마 유래는 민간 전설이고 그 전부터 쓰인 말이라는 기록이 있으니 자막으로 밝힌다.

