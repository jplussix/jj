#!/usr/bin/env python3
"""Episode 1 rough cut: join finished clips, burn subtitles, add BGM (ducked) and gag SFX.

Order: 01 -> title -> "열여덟 시간 전" -> 02A -> 03 -> 04A -> 04B -> 05A -> 05B -> 06A -> 06B -> 06C -> 07A -> 07B -> 07C -> 07D -> 07D2 -> 07E -> 07F -> 07G -> 07H -> 08A -> 08B.
Transitions are per-segment fades (no overlap, so subtitle times stay simple):
black dips between scenes, a white flash + whoosh/boom for the jump into Joseon.
Subtitle times come from the ElevenLabs transcripts of each clip (word timestamps).
Output: renders/ep01/ep01_roughcut_v3.mp4
"""
import os
import subprocess

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TMP = os.environ.get("CUT_TMP", "/tmp/roughcut")
os.makedirs(TMP, exist_ok=True)
R = lambda p: os.path.join(ROOT, p)  # noqa: E731

SEGMENTS = [  # (file, duration, start offset in source, (fade-in colour, secs), (fade-out colour, secs))
    ("renders/ep01/clip01_take1.mp4", 25.056, 0, ("black", 0.8), None),  # inner VO now mixed from VO list
    ("assets/title/title_sequence_480p.mp4", 4.742, 1.3, None, None),  # skip 1.3 s of silent lead-in; drum hit lands at 0.9 s
    ("CARD", 2.0, 0, None, None),
    ("renders/ep01/clip02a_take2.mp4", 25.056, 0, ("black", 0.6), ("black", 0.5)),
    ("renders/ep01/clip03_take1_claude.mp4", 28.0, 2.0, ("black", 0.5), ("black", 0.6)),  # first 2s far wide cut
    ("renders/ep01/clip04a_take2.mp4", 23.0, 0, ("black", 0.6), ("black", 0.25)),
    ("renders/ep01/clip04b_take2.mp4", 10.0, 0, ("black", 0.25), ("white", 0.45)),
    ("renders/ep01/clip05a_take1.mp4", 30.08, 0, ("white", 0.9), None),
    ("renders/ep01/clip05b_combined.mp4", 31.48, 0, None, ("black", 0.5)),
    ("renders/ep01/clip06a_combined.mp4", 25.6, 0, ("black", 0.6), ("black", 0.35)),
    ("renders/ep01/clip06b_seedance.mp4", 24.06, 0, ("black", 0.35), None),
    ("renders/ep01/clip06c_take1.mp4", 28.05, 0, None, ("black", 0.5)),
    ("renders/ep01/clip07a_take1.mp4", 25.79, 0, ("black", 0.5), None),  # cut before the over-acted laugh (shot change at 25.83)
    ("renders/ep01/clip07a_laugh_fix.mp4", 4.0, 0, None, ("black", 0.25)),  # restrained laugh re-shoot
    ("renders/ep01/clip07b_combined.mp4", 24.45, 0, ("black", 0.25), None),  # take1 0-18.375 + dry-face ending
    ("renders/ep01/clip07c_fix.mp4", None, 0, None, None),      # "장강님" cut out
    ("renders/ep01/clip07d_fix.mp4", None, 0, None, None),      # "장장님" cut out
    ("renders/ep01/clip07d2_take1.mp4", None, 0, None, ("black", 0.4)),
    ("renders/ep01/clip07e_fix.mp4", None, 0, ("black", 0.4), None),  # "장강님" cut out
    ("renders/ep01/clip07f_combined.mp4", None, 0, None, None),  # gate-opening shot dropped (bar stayed on)
    ("renders/ep01/clip07g_take1.mp4", None, 0, None, None),
    ("renders/ep01/clip07h_take1.mp4", None, 0, None, ("white", 0.45)),
    ("renders/ep01/clip08a_take1.mp4", None, 0, ("white", 0.9), ("black", 0.3)),
    ("renders/ep01/clip08b_take1.mp4", None, 0, ("black", 0.3), ("black", 1.5)),
]
AV_SHIFT = 0.0  # whole-episode dialogue shift (none: only 07F needed it)
# Per-clip dialogue shift in seconds (audio pulled earlier). User A/B: 07F lips matched at -60 ms; other clips were fine.
CLIP_AUDIO_SHIFT = {"renders/ep01/clip07f_combined.mp4": 0.06}


def _dur(path):
    out = subprocess.run(["ffprobe", "-v", "error", "-show_entries", "format=duration", "-of", "csv=p=0", R(path)],
                         capture_output=True, text=True).stdout
    return round(float(out) - 0.05, 3)


# frame-align every segment (24 fps) so audio and video have exactly the same length; otherwise the
# concat drifts ~0.01-0.04 s per segment and lip sync is ~0.25 s off by the last scene.
SEGMENTS = [(f, int((d if d is not None else _dur(f)) * 24) / 24, o, fi, fo) for f, d, o, fi, fo in SEGMENTS]
starts, t = [], 0.0
for seg in SEGMENTS:
    starts.append(t)
    t += seg[1]
TOTAL = t
S01, STITLE, SCARD, S02A, S03, S04A, S04B, S05A, S05B, S06A, S06B, S06C, S07A, S07AL, S07B, S07C, S07D, S07D2, S07E, S07F, S07G, S07H, S08A, S08B = starts

# (start, end, style, text). 03 times: scribe transcript minus the 2s trim.
# 04A take2 / 05B: not transcribed (credits) - estimated from take1 / prompt timeline.
SUBS = [
    (S01 + 0.8, S01 + 5.0, "Place", "세종 16년(1434), 함길도 북방 삭풍진"),
    (S01 + 1.5, S01 + 4.7, "Inner", "(속마음) 여기 어디야… 웬 불이 저렇게 많아."),
    (S01 + 9.2, S01 + 11.9, "Line", "적이 육천입니다. 아군은 팔백입니다."),
    (S01 + 11.75, S01 + 15.0, "Inner", "(속마음) 육천? 팔백? …재고 얘긴가."),
    (S01 + 15.05, S01 + 17.7, "Line", "장군, 명을 내리소서."),
    (S01 + 18.0, S01 + 20.2, "Inner", "(속마음) 장군? 나한테 하는 소리야?"),
    (SCARD + 0.2, SCARD + 1.9, "Card", "18시간 전"),
    (S02A + 0.42, S02A + 3.6, "Line", "부장님… 아니, 선배님. 저도 마음이 안 좋습니다."),
    (S02A + 4.68, S02A + 6.95, "Line", "최 대리… 아, 상무님."),
    (S02A + 7.6, S02A + 9.8, "Line", "우리 애 취직할 때까지만요. 일 년만."),
    (S02A + 10.7, S02A + 12.3, "Line", "본사 결재가 어제 끝났어요."),
    (S02A + 17.0, S02A + 18.7, "Line", "제가 여기서 이십칠 년입니다."),
    (S02A + 19.2, S02A + 21.2, "Line", "그래서 위로금도 넉넉히 넣었습니다."),
    (S03 + 1.3, S03 + 3.7, "Line", "쉰넷. 나이가 좀 많으시네."),
    (S03 + 4.5, S03 + 5.7, "Line", "체력은 자신 있습니다."),
    (S03 + 6.3, S03 + 10.1, "Line", "물류센터 부장을 하셨네. 경비 일은 해 보셨어요?"),
    (S03 + 12.5, S03 + 13.8, "Line", "그럼 특기가 뭡니까?"),
    (S03 + 14.5, S03 + 15.6, "Line", "재고 조사입니다."),
    (S03 + 19.0, S03 + 19.9, "Line", "재고 조사."),
    (S03 + 20.3, S03 + 22.5, "Line", "숫자하고 물건이 안 맞으면 잠이 안 옵니다."),
    (S03 + 23.2, S03 + 25.8, "Line", "저거나 좀 맞춰 봐요. 내일부터 야간입니다."),
    (S04A + 3.7, S04A + 5.0, "Line", "저기, 내가 할 말이."),
    (S04A + 5.6, S04A + 8.6, "Line", "여보, 이번 달 대출 이자 또 올랐어."),
    (S04A + 10.3, S04A + 12.0, "Line", "하은아, 면접은."),
    (S04A + 13.0, S04A + 14.4, "Line", "아빠는 몰라도 돼."),
    (S04A + 17.3, S04A + 18.7, "Line", "회사는 별일 없지?"),
    (S04A + 20.3, S04A + 21.6, "Line", "별일 없지."),
    (S04B + 4.2, S04B + 6.5, "Line", "(TV) 전군, 나를 따르라!"),
    (S05A + 3.6, S05A + 5.0, "Line", "아이고…"),
    (S05A + 9.0, S05A + 10.4, "Line", "안 아프네."),
    (S05A + 26.6, S05A + 28.3, "Line", "누구세요."),
    (S05B + 2.3, S05B + 4.0, "Line", "장군, 기침하셨습니까."),
    (S05B + 5.2, S05B + 7.0, "Line", "저, 실례지만 어디서 오셨어요?"),
    (S05B + 7.3, S05B + 10.0, "Line", "장군, 어찌 소인한테 존대를 하십니까?"),
    (S05B + 10.3, S05B + 14.0, "Line", "아, 그러니까. 그대는, 누구시, 누구시오. 누구냐."),
    (S05B + 14.3, S05B + 17.0, "Line", "군관 천봉수입니다. 십 년을 모셨습니다."),
    (S05B + 18.2, S05B + 21.0, "Line", "열은 없으신데, 말씀이 영 이상하십니다."),
    (S05B + 21.1, S05B + 24.1, "Line", "적이 진을 쳤습니다. 성루로 가셔야 합니다."),
    # 06A-06C: not transcribed (credits) - placed from speech-band envelope + prompt timeline.
    # 06A-06C: retimed with local Whisper (user: subtitles off at "창고 갑시다").
    (S06A + 0.0, S06A + 3.1, "Line", "적이 육천입니다."),
    (S06A + 3.4, S06A + 4.7, "Line", "아군은 팔백입니다."),
    (S06A + 5.0, S06A + 6.85, "Line", "장군, 명을 내리소서."),
    (S06A + 8.35, S06A + 11.05, "Line", "일단 회의부터 합시다."),
    (S06A + 11.85, S06A + 15.1, "Line", "장군, 저희한테 '합시다'라니요."),
    (S06A + 15.35, S06A + 17.3, "Line", "그리고 회의가 무엇입니까?"),
    (S06A + 18.0, S06A + 19.5, "Line", "다 같이 앉아서 얘기하는 거예요."),
    (S06A + 21.1, S06A + 23.2, "Line", "아니, …것이오. 것이다!"),
    (S06B + 2.0, S06B + 4.9, "Line", "장군님 말씀이 왜 저러시나."),
    (S06B + 5.7, S06B + 8.8, "Line", "어젯밤에 말에서 떨어지셨다던데."),
    (S06B + 12.3, S06B + 15.1, "Line", "먼저 현황부터. 쌀이 얼마나 남았소?"),
    (S06B + 16.0, S06B + 18.1, "Line", "삼백 석입니다. 넉 달은 버팁니다."),
    (S06B + 20.4, S06B + 21.4, "Line", "장부 좀 봅시다."),
    (S06C + 2.3, S06C + 6.75, "Line", "지난달에 이백 석이 들어왔는데, 나간 건 오십 석이네."),
    (S06C + 7.8, S06C + 8.6, "Line", "그렇습니다."),
    (S06C + 9.8, S06C + 13.0, "Line", "그 전에 남은 게 백오십 석. 합치면 삼백 석."),
    (S06C + 13.2, S06C + 14.3, "Line", "숫자는 맞소."),
    (S06C + 14.7, S06C + 18.2, "Line", "그런데 받은 사람 수결이 석 달째 한 사람 글씨요."),
    (S06C + 20.1, S06C + 22.45, "Line", "입고하는 사람하고 확인하는 사람이 같으면 안 되지."),
    (S06C + 22.6, S06C + 23.3, "Line", "창고 갑시다."),
    (S06C + 23.65, S06C + 24.6, "Line", "지금 말입니까?"),
    (S06C + 25.2, S06C + 26.2, "Line", "적이 코앞인데."),
    (S06C + 26.55, S06C + 27.7, "Line", "그러니까 지금 세야지."),
    (S07A + 0.5, S07A + 3.5, "Place", "군량 창고"),
    (S07A + 2.0, S07A + 3.05, "Line", "한 줄에 열 섬씩."),
    (S07A + 3.5, S07A + 5.2, "Line", "줄 맞춰 다시 쌓으시오."),
    (S07A + 8.75, S07A + 11.3, "Line", "열, 열하나, 열둘."),
    (S07A + 11.7, S07A + 12.55, "Line", "열두 줄입니다."),
    (S07A + 13.5, S07A + 14.3, "Line", "백이십 석."),
    (S07A + 16.0, S07A + 18.4, "Line", "백여든 석이 빕니다."),
    (S07A + 20.0, S07A + 21.3, "Line", "쥐가 들었나 봅니다."),
    (S07A + 21.6, S07A + 25.8, "Line", "쥐가 백여든 석을 먹으면 소만 해졌겠소."),
    (S07B + 2.6, S07B + 5.5, "Line", "장군님께서 언제부터 셈에 그리 밝으셨습니까."),
    (S07B + 7.4, S07B + 9.2, "Line", "(밖에서) 기병이다! 성문으로 온다!"),
    (S07B + 10.75, S07B + 12.6, "Line", "(밖에서) 아니다! 우리 깃발이다!"),
    (S07B + 12.95, S07B + 14.8, "Line", "(밖에서) 도절제사 영감이시다!"),
    (S07B + 15.2, S07B + 18.2, "Line", "장군님, 대호께서 오셨습니다. 하필 오늘."),
    (S07B + 20.75, S07B + 22.3, "Line", "본사 감사가 왜 하필 지금."),
    # 07C-08B: times from local Whisper (tools/transcribe.py), text from the script.
    (S07C + 1.4, S07C + 4.75, "Line", "빈 가마니에 짚을 채워 앞줄만 다시 메워라."),
    (S07C + 5.2, S07C + 6.2, "Line", "어서."),
    (S07C + 7.4, S07C + 9.3, "Line", "손대지 마시오."),
    (S07C + 10.45, S07C + 12.1, "Line", "도절제사 영감이십니다."),
    (S07C + 12.3, S07C + 13.8, "Line", "빈자리를 보이면 끝장입니다."),
    (S07C + 14.8, S07C + 18.1, "Line", "빈자리를 가짜로 채우면 그건 사기요."),
    (S07C + 18.4, S07C + 22.6, "Inner", "(속마음) 감사 나왔는데 분식회계를 하라고? 걸리면 내가 독박이지."),
    (S07D + 2.3, S07D + 6.05, "Line", "달마다 올린 군량 보고서에 장군님 직인도 찍혀 있습니다."),
    (S07D + 7.6, S07D + 10.85, "Line", "백여든 석이 비면 소인만 죽는 게 아닙니다."),
    (S07D + 11.1, S07D + 13.1, "Line", "전시 군량 축내는 건 참수입니다."),
    (S07D + 13.6, S07D + 14.6, "Line", "일단 덮으시지요."),
    (S07D2 + 1.9, S07D2 + 4.05, "Line", "숨기다 걸리면 가중처벌이오."),
    (S07D2 + 5.0, S07D2 + 6.4, "Line", "자진 신고부터 해야지."),
    (S07D2 + 7.5, S07D2 + 9.3, "Line", "자진… 뭐, 뭐라 하셨습니까?"),
    (S07D2 + 11.85, S07D2 + 13.05, "Line", "창고 문 활짝 열어 두시오."),
    (S07D2 + 13.7, S07D2 + 15.1, "Line", "내가 직접 브리핑하겠소."),
    (S07D2 + 15.5, S07D2 + 16.4, "Line", "아니, 고하겠소!"),
    (S07E + 0.5, S07E + 3.3, "Place", "성문 안 마당"),
    (S07E + 0.35, S07E + 3.4, "Inner", "(속마음) 김종서? 교과서에 나오는 그 대호?"),
    (S07E + 3.5, S07E + 10.0, "Line", "영감께서 눈을 마주치시면 무조건 죽여 달라고 하십시오."),
    (S07E + 10.8, S07E + 12.8, "Line", "일하러 온 사람한테 왜 죽여 달라고 해요?"),
    (S07E + 13.6, S07E + 14.3, "Line", "아니, 하느냐."),
    (S07E + 14.4, S07E + 21.9, "Line", "지난달에 옆 진 첨절제사는 장부 한 줄 틀렸다고 곤장 스무 대에 파직당했습니다."),
    (S07E + 22.5, S07E + 26.9, "Inner", "(속마음) 한 줄에 곤장 스무 대? …여긴 백여든 석이 비는데."),
    (S07F + 3.4, S07F + 8.05, "Line", "지금이라도 창고 문을 닫고 쥐 핑계를 대시지요."),
    (S07F + 8.9, S07F + 13.4, "Line", "소만 한 쥐가 먹었다고 하면 곤장이 아니라 칼이 날아오겠소."),
    (S07F + 14.2, S07F + 17.15, "Line", "(혼잣말) 안녕하십니까, 도절제사님."),
    (S07F + 17.7, S07F + 19.85, "Line", "삭풍진 재고 감사 보고드리겠습니다."),
    (S07F + 21.2, S07F + 23.9, "Line", "가, 감… 뭐라 하셨습니까?"),
    (S07G + 4.2, S07G + 7.3, "Line", "도절제사 영감, 뵙습니다!"),
    (S07G + 10.5, S07G + 13.6, "Line", "먼 길 오시느라 고생 많으셨습니다."),
    (S07G + 18.0, S07G + 20.4, "Inner", "(속마음) 아우, 무릎이야."),
    (S07H + 4.1, S07H + 6.5, "Line", "창고 문이 열려 있구나."),
    (S07H + 10.0, S07H + 14.1, "Inner", "(속마음) 나랑 나이도 비슷한데… 눈빛이 상무님보다 무섭네."),
    (S07H + 14.7, S07H + 16.2, "Line", "군량이 몇 석이냐."),
    (S08A + 2.5, S08A + 4.7, "Line", "여보, 출근 안 해?"),
    (S08A + 7.7, S08A + 8.9, "Line", "백이십 석."),
    (S08A + 9.7, S08A + 12.0, "Line", "백이십 석 같은 소리 하고 있네."),
    (S08A + 12.3, S08A + 13.7, "Line", "일곱 시 반이야!"),
    (S08A + 15.0, S08A + 16.2, "Line", "아이고."),
    (S08A + 17.3, S08A + 19.6, "Inner", "(속마음) 꿈이었나…"),
    (S08B + 1.6, S08B + 3.9, "Line", "아빠, 그걸 왜 찾아?"),
    (S08B + 5.9, S08B + 8.3, "Line", "팔백 명을 먹여야 돼서."),
]
SFX = [  # (time, file, volume)
    # Sound design under Han's frozen face into the title (user: the gap before the title felt empty):
    # low drone swell + accelerating heartbeat + riser, all landing on the title's drum hit.
    (S01 + 20.0, "audio/sfx/drone_swell.wav", 0.75),
    (S01 + 20.4, "audio/sfx/heartbeat.wav", 0.85),
    (STITLE - 1.7, "audio/sfx/riser.wav", 0.8),          # builds into the title drum (title 2.2 s - 1.3 s offset)
    (SCARD + 0.0, "audio/sfx/clock_tick.wav", 0.7),     # "18시간 전" card
    (S05A + 27.4, "audio/sfx/gag_boing.mp3", 0.8),
    (S05B + 26.2, "audio/sfx/gag_boing.mp3", 0.9),
    (S05A - 0.45, "audio/sfx/trans_whoosh.wav", 0.9),   # jump into Joseon (white flash)
    (S05A - 0.05, "audio/sfx/trans_boom.wav", 0.9),
    (S06A + 10.9, "audio/sfx/gag_crickets.mp3", 0.7),  # silence after "회의부터 합시다"
    (S07D2 + 6.5, "audio/sfx/gag_crickets.mp3", 0.6),   # silence after "자진 신고부터 해야지"
    (S07G + 16.6, "audio/sfx/gag_boing.mp3", 0.7),      # as his knee is yanked down to the stone
    (S07G - 0.6, "audio/sfx/gate_open.wav", 0.8),       # gate opens over the cut (gate shot dropped)
    (S07H + 17.6, "audio/sfx/phone_alarm.wav", 0.35),   # alarm bleeds in before the white flash
    (S07H + 19.4, "audio/sfx/trans_whoosh.wav", 0.7),
]
# Park Mansu inner monologue: eleven_v4, cloned from his on-screen Seedance voice
# (voice_id 2QR7415RxATcyYH6g8Rd, sample audio/voice_clone/parkmansu_seedance_sample.mp3).
VO = [  # (time, file, volume) - v2: emotion tags, speed 1.12, placed in the gaps between lines
    (S01 + 1.5, "audio/ep01/inner/v2/01a.mp3", 1.0),
    (S01 + 11.75, "audio/ep01/inner/v2/01b_fx.mp3", 1.0),   # atempo 1.2 to fit before Cheon's next line
    (S01 + 18.0, "audio/ep01/inner/v2/01c_fx.mp3", 1.0),    # doubled "장군?" trimmed
    (S07C + 18.4, "audio/ep01/inner/v2/07c.mp3", 1.0),
    (S07E + 0.35, "audio/ep01/inner/v2/07e1.mp3", 1.0),     # shortened text, ends before Cheon at 3.5
    (S07E + 22.5, "audio/ep01/inner/v2/07e2.mp3", 1.0),     # a beat after Cheon's line (user: came in too fast)
    (S07G + 18.0, "audio/ep01/inner/v2/07g.mp3", 1.0),
    (S07H + 10.0, "audio/ep01/inner/v2/07h.mp3", 1.0),
    (S08A + 17.3, "audio/ep01/inner/v2/08a_fx.mp3", 1.0),   # doubled "꿈이었나?" trimmed
]

BGM = [  # (file, start, end, source offset, volume) - user: BGM was too loud and wrong in many places.
    # Cue-based: music under openings, transitions and key beats only; quieter; ducked hard under speech.
    ("audio/bgm/02_joseon_tension.mp3", S01, STITLE + 1.0, 0.0, 0.16),     # cold open, carries into the title
    ("audio/bgm/05_bittersweet.mp3", SCARD, S02A + 25.0, 0.0, 0.12),
    ("audio/bgm/04_modern_daily.mp3", S03, S03 + 12.0, 0.0, 0.09),
    ("audio/bgm/05_bittersweet.mp3", S04A, S04A + 23.0, 30.0, 0.11),
    ("audio/bgm/03_mansu_fumble.mp3", S05A + 5.0, S05A + 30.0, 0.0, 0.10),
    ("audio/bgm/03_mansu_fumble.mp3", S06A + 0.5, S06A + 12.0, 60.0, 0.09),
    ("audio/bgm/02_joseon_tension.mp3", S06C + 12.0, S06C + 28.0, 40.0, 0.12),
    ("audio/bgm/02_joseon_tension.mp3", S07B + 6.0, S07B + 24.4, 70.0, 0.12),
    ("audio/bgm/02_joseon_tension.mp3", S07G, S07H + 19.5, 0.0, 0.13),     # Kim Jongseo arrives
    ("audio/bgm/04_modern_daily.mp3", S08A + 16.0, S08B + 12.0, 0.0, 0.09),
]


def ts(x):
    h, m = int(x // 3600), int(x % 3600 // 60)
    return f"{h}:{m:02d}:{x % 60:05.2f}"


def write_ass(path):
    head = """[Script Info]
ScriptType: v4.00+
PlayResX: 854
PlayResY: 480

[V4+ Styles]
Format: Name, Fontname, Fontsize, PrimaryColour, SecondaryColour, OutlineColour, BackColour, Bold, Italic, Underline, StrikeOut, ScaleX, ScaleY, Spacing, Angle, BorderStyle, Outline, Shadow, Alignment, MarginL, MarginR, MarginV, Encoding
Style: Line,NanumGothic,26,&H00FFFFFF,&H00FFFFFF,&H00000000,&H64000000,1,0,0,0,100,100,0,0,1,2.4,0,2,30,30,26,1
Style: Inner,NanumGothic,25,&H0060E8FF,&H0060E8FF,&H00000000,&H64000000,1,0,0,0,100,100,0,0,1,2.4,0,2,30,30,62,1
Style: Place,NanumMyeongjo,22,&H00FFFFFF,&H00FFFFFF,&H00000000,&H64000000,1,0,0,0,100,100,0,0,1,1.8,0,7,34,30,30,1
Style: Card,Nanum Pen Script,64,&H006DC4F2,&H006DC4F2,&H00102030,&H00000000,0,0,0,0,100,100,1,0,1,1.2,0,5,30,30,30,1

[Events]
Format: Layer, Start, End, Style, Name, MarginL, MarginR, MarginV, Effect, Text
"""
    with open(path, "w", encoding="utf-8") as f:
        f.write(head)
        for a, b, st, txt in SUBS:
            if st == "Place":
                continue  # user: no location captions
            fade = r"{\fad(300,300)}" if st in ("Place", "Card") else r"{\fad(80,80)}"
            f.write(f"Dialogue: 0,{ts(a)},{ts(b)},{st},,0,0,0,,{fade}{txt}\n")


def run(cmd):
    subprocess.run(cmd, check=True)


def main():
    norm = []
    for i, (src, dur, off, fin, fout) in enumerate(SEGMENTS):
        vf, af = [], []
        if fin:
            vf.append(f"fade=t=in:st=0:d={fin[1]}:c={fin[0]}")
            af.append(f"afade=t=in:st=0:d={min(fin[1], 0.4)}")
        if fout:
            vf.append(f"fade=t=out:st={dur - fout[1]:.3f}:d={fout[1]}:c={fout[0]}")
            af.append(f"afade=t=out:st={dur - min(fout[1], 0.4):.3f}:d={min(fout[1], 0.4)}")
        vfx = ("," + ",".join(vf)) if vf else ""
        afx = ("," + ",".join(af)) if af else ""
        out = os.path.join(TMP, f"seg{i}.mp4")
        if src == "CARD":
            run(["ffmpeg", "-nostdin", "-v", "error", "-y", "-f", "lavfi", "-i", f"color=c=black:s=854x480:r=24:d={dur}",
                 "-f", "lavfi", "-i", f"anullsrc=r=48000:cl=stereo", "-t", str(dur),
                 "-c:v", "libx264", "-pix_fmt", "yuv420p", "-c:a", "aac", "-shortest", out])
        else:
            run(["ffmpeg", "-nostdin", "-v", "error", "-y", "-ss", str(off), "-i", R(src), "-vf", "scale=854:480,fps=24,setsar=1" + vfx,
                 "-af", (f"atrim=start={CLIP_AUDIO_SHIFT[src]},asetpts=PTS-STARTPTS," if src in CLIP_AUDIO_SHIFT else "") + "aresample=48000,aformat=channel_layouts=stereo" + afx + f",apad,atrim=0:{dur}", "-t", str(dur),
                 "-c:v", "libx264", "-pix_fmt", "yuv420p", "-crf", "18", "-c:a", "aac", "-b:a", "192k", out])
        norm.append(out)
    lst = os.path.join(TMP, "list.txt")
    with open(lst, "w") as f:
        f.writelines(f"file '{p}'\n" for p in norm)
    base = os.path.join(TMP, "base.mp4")
    run(["ffmpeg", "-nostdin", "-v", "error", "-y", "-f", "concat", "-safe", "0", "-i", lst, "-c", "copy", base])

    ass = os.path.join(TMP, "subs.ass")
    write_ass(ass)

    inputs = ["-i", base]
    fc = []
    vo_labels = []
    for k, (tm, f, vol) in enumerate(VO):
        inputs += ["-i", R(f)]
        fc.append(f"[{len(inputs)//2 - 1}:a]aresample=48000,aformat=channel_layouts=stereo,volume={vol},"
                  f"adelay={int(tm*1000)}|{int(tm*1000)}[vo{k}]")
        vo_labels.append(f"[vo{k}]")
    fc.append(f"[0:a]atrim=start={AV_SHIFT},asetpts=PTS-STARTPTS,apad=whole_dur={TOTAL:.3f}[src]")
    fc.append("[src]" + "".join(vo_labels) + f"amix=inputs={len(vo_labels)+1}:normalize=0:duration=first[base]")
    fc.append("[base]asplit=2[dia][key]")
    mix = ["[dia]"]
    n = 1 + len(VO)  # inputs 1..len(VO) are the inner-monologue VO files
    bgm_labels = []
    for k, (f, a, b, off, vol) in enumerate(BGM):
        inputs += ["-ss", str(off), "-i", R(f)]
        d = b - a
        fc.append(f"[{n}:a]atrim=0:{d:.3f},asetpts=PTS-STARTPTS,afade=t=in:d=1.0,afade=t=out:st={d-1.5:.3f}:d=1.5,"
                  f"volume={vol},adelay={int(a*1000)}|{int(a*1000)},apad=whole_dur={TOTAL:.3f}[b{k}]")
        bgm_labels.append(f"[b{k}]")
        n += 1
    fc.append("".join(bgm_labels) + f"amix=inputs={len(bgm_labels)}:normalize=0[bgm]")
    fc.append("[bgm][key]sidechaincompress=threshold=0.012:ratio=20:attack=10:release=600[bgmd]")
    mix.append("[bgmd]")
    for k, (tm, f, vol) in enumerate(SFX):
        inputs += ["-i", R(f)]
        fc.append(f"[{n}:a]volume={vol},adelay={int(tm*1000)}|{int(tm*1000)}[s{k}]")
        mix.append(f"[s{k}]")
        n += 1
    fc.append("".join(mix) + f"amix=inputs={len(mix)}:normalize=0:duration=first,loudnorm=I=-14:TP=-1.5:LRA=11,volume=2.4dB,alimiter=limit=0.84:level=false[aout]")
    fc.append(f"[0:v]ass={ass}[vout]")
    out = R("renders/ep01/ep01_roughcut_v3.mp4")
    run(["ffmpeg", "-nostdin", "-v", "error", "-y", *inputs, "-filter_complex", ";".join(fc), "-map", "[vout]", "-map", "[aout]",
         "-c:v", "libx264", "-pix_fmt", "yuv420p", "-crf", "18", "-c:a", "aac", "-b:a", "192k", "-ar", "48000", out])
    print(f"{out} ({TOTAL:.1f}s)")


if __name__ == "__main__":
    main()
