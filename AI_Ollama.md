### Ollama




qwen3-coder:latest

claude --model qwen3-coder:latest


❯ 디렉토리 구조를 살펴봐
  ⎿  Credit balance too low · Add funds: https://platform.claude.com/settings/billing

Aider와 Ollama

aider --model ollama/qwen3-coder:latest







Connect device
Connect toby-MacBookPro.local with namkikim4071

This device will be paired with your account.

ssh-ed25519 AAAAC3NzaC1lZDI1NTE5AAAAIFSkB7sqkYoZ7/o3nFhSFTxdBOC2ZPmHtSwx+/gFZD+M





npm i -g @continuedev/cli && cn "Explore this repo and provide a concise summary of it's contents"

npm install -g @continuedev/cli

4단계: 터미널에서 Continue 활용하기
① 대화형 인터랙티브 모드 (TUI Mode)
cn

② 단발성 명령 실행 모드 (Headless Mode)
cn -p "파이썬에서 리스트를 역순으로 정렬하는 함수를 작성해줘"





Benchmark
MMLU (5-shot)
Open-rewrite eval (0-shot, rougeL)
TLDR9 + (test, 1-shot, rougeL)
IFEval
Tool Use
BFCL V2
Nexus
Math
GSM8K (8-shot, CoT)
MATH (O-shot, CoT)
Reasoning
ARC Challenge (O-shot)
GPOA (o-shot)|
Hellaswag (0-shot)
Long Context
InfiniteBench/En.MC (128k))
InfiniteBench/En.QA (128k)
NIH/Multi-needle
Multilingual
MGSM (O-shot, CoT)

1. 일반 지식 및 지시 이행 (General Knowledge & Instruction)
- MMLU (5-shot)설명: 인문학, 사회과학, STEM 등 57개 과목의 전문가 수준 객관식 문제를 풀게 하여 모델의 사전 지식과 상식을 평가합니다.조건: 5-shot은 문제를 풀기 전 5개의 예시(질문+정답)를 미리 보여주어 힌트를 준 상태에서 평가함을 뜻합니다.
- Open-rewrite eval (0-shot, rougeL)설명: 모델에게 입력된 문장이나 글을 특정 요구사항(예: 더 정중하게, 요약해서, 문체 변경 등)에 맞게 다시 작성(Rewriting)하는 능력을 평가합니다.조건: 0-shot은 예시 없이 바로 수행하며, rougeL 지표를 통해 정답 텍스트와 모델이 생성한 텍스트 간의 최장 공통 부분 수열(LCS) 유사도를 측정해 채점합니다.
- TLDR9+ (test, 1-shot, rougeL)설명: 주로 Reddit 등의 긴 글을 한 줄 요약(TL;DR)하는 능력을 측정하기 위한 텍스트 요약 성능 평가용 테스트 데이터셋입니다.조건: 1-shot은 요약 예시를 딱 1개 보여준 후 수행하며, 요약의 정확성을 rougeL 지표로 평가합니다.
- IFEval (Instruction Following Evaluation)설명: 모델이 "글자 수를 300자 이하로 제한해라", "JSON 형식으로만 출력해라", "특정 단어를 포함하지 마라"와 같이 텍스트의 형태와 제약 조건을 엄격히 지키는 지시 이행 능력을 검증합니다.
2. 도구 활용 및 에이전트 능력 (Tool Use & Agent)
- Tool Use설명: AI가 단순 답변을 넘어 외부 API, 계산기, 웹 검색 등의 도구를 적절한 타이밍에 호출하여 연동하는 능력을 종합적으로 평가합니다.
- BFCL V2 (Berkeley Function Calling Leaderboard V2)설명: UC 버클리에서 개발한 벤치마크로, 모델이 사용자의 요청을 분석하여 정확한 함수(Function)를 호출하고 필요한 인자(Arguments)를 올바르게 채워 넣는지를 매우 까다롭게 평가하는 업계 표준 지표입니다.
- Nexus설명: 복잡하고 연쇄적인 API 호출이나 도구 활용, 에이전트(Agent)로서의 워크플로우 수행 능력을 측정하는 벤치마크입니다.
3. 수학 및 추론 (Math & Reasoning)
- GSM8K (8-shot, CoT)설명: 초등학교 수준의 문장제 수학 문장(Grade School Math) 8,500개로 구성된 데이터셋입니다. 사칙연산을 조합하여 단계를 거쳐 풀어야 합니다.조건: 8-shot으로 8개의 예시를 주며, CoT(Chain-of-Thought, 생각의 사슬) 기법을 적용하여 모델이 중간 풀이 과정을 논리적으로 서술하며 정답에 도달하도록 유도합니다.
- MATH (0-shot, CoT)설명: 고등학교 수학 경시대회 수준의 매우 어려운 주관식 수학 문제들로 구성되어 있어 LLM에게 가장 까다로운 수학 데이터셋 중 하나입니다.조건: 예시 없이(0-shot) 단계별 논리적 풀이 과정(CoT)을 거쳐 최종 수식 정답을 맞혀야 합니다.
- ARC Challenge (0-shot) (AI2 Reasoning Challenge)설명: 초등학교 및 중학교 수준의 과학 시험 문제 중, 단순 암기가 아닌 실제 인과관계 추론 및 과학적 상식 결합이 필요한 고난도 문항만 모아놓은 벤치마크입니다.
- GPQA (0-shot) (오타 GPOA 수정)설명: 생물학, 물리학, 화학 분야의 PhD(박사)급 전문가들이 출제한 대학원 수준의 초고난도 과학 문제 데이터셋입니다. 검색을 허용해도 일반인은 풀지 못하는 "Google-proof(구글링 방지)" 문제들로 구성되어 모델의 순수 추론 능력을 극한으로 시험합니다.
- Hellaswag (0-shot)설명: 어떤 상황을 묘사한 문장을 주고, 그다음에 이어질 가장 자연스러운 행동이나 상황을 객관식으로 맞히는 벤치마크입니다. 인간에게는 너무 당연한 '상식적 추론(Commonsense Reasoning)'을 AI가 잘 이해하는지 검증합니다.
4. 긴 문맥 이해 (Long Context)
- InfiniteBench/En.MC (128k)설명: 10만 토큰 이상의 초장문(Long-Context) 처리 능력을 검증하는 인피니트벤치 데이터셋 중 하나입니다. 영어 소설이나 긴 텍스트(약 128k 분량)를 통째로 입력한 뒤, 본문 내용을 바탕으로 한 객관식 문제(Multiple Choice)를 풀게 합니다.
- InfiniteBench/En.QA (128k)설명: 위와 동일하게 128k 수준의 방대한 텍스트를 입력한 뒤, 본문 내용에 대해 주관식 질의응답(Quality Assurance)을 수행하여 정확한 답변을 찾아내는지 평가합니다.
- NIH/Multi-needle (Needle In A Haystack)설명: '건더미 속에서 바늘 찾기' 테스트입니다. 방대한 문서 데이터 사이에 아무 상관 없는 무작위 정보(바늘)를 숨겨놓고, 모델이 그 숨겨진 정보를 완벽하게 찾아내어 기억(Recall)하는지 평가하는 기법입니다. Multi-needle은 숨겨놓은 바늘이 여러 개일 때 이를 모두 놓치지 않고 회수하는지 검증합니다.
5. 다국어 능력 (Multilingual)
- MGSM (0-shot, CoT) (Multilingual Grade School Math)설명: 위에서 언급한 초등 수학 벤치마크인 GSM8K를 세계 각국의 다양한 언어로 번역한 다국어 버전입니다. 모델이 영어뿐만 아니라 다른 언어로 된 수학 문제를 받았을 때도 번역 오류 없이 문제를 정확히 이해하고 단계별(CoT)로 추론하여 정답을 도출하는지 평가합니다.추가로 이 중에서 특정 벤치마크의 실제 문제 예시를 보고 싶으시거나, 특정 모델(예: Llama 3, GPT-4o)의 실제 합격 점수 비교가 필요하시면 말씀해 주세요!
