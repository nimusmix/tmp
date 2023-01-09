## React TypeScript Props 관련 TypeError 도와주세요.

[Q&A 링크](https://google.com)

<br/>

### 에러 코드

Type '{ code ... }' is not assignable to type 'IntrinsicAttributes'

<br/>

### 질문 내용

TypeScript로 리액트 코드를 작성하여 props를 넘겨주는 과정에서 위와 같은 에러가 발생합니다.

잘 동작하던 코드인데 이유가 뭘까요..? 도와주세요..

<br/>

### 내 답변

JavaScript 코드를 TypeScript로 변환하는 과정에서 타입을 지정해주지 않아 발생한 문제로 보입니다.

해당 코드의 interface를 확인하여 적절한 데이터 타입을 지정해주세요.