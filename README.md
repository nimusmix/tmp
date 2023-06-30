# CHECK YOUR SITE

10년 간의 홈페이지 변화를 확인할 수 있는 사이트

<br/>

### 🚀 서비스 링크

https://check-your-site.netlify.app/

<br/>

### 🖥️ 주요 기능

**관심 사이트 목록**

- 원하는 사이트를 관심 사이트 목록에 등록할 수 있습니다.
- 최대 4개까지 등록이 가능하고, 초과 시 경고가 노출되며 등록되지 않습니다.
- 등록된 카드를 hovering하면 상세 페이지 이동 버튼과 카드 삭제 버튼을 보여줍니다.
- 카드가 등록되지 않았을 때도 4개의 빈 카드를 보여주어
    사이트를 최대 4개까지 등록할 수 있다는 점을 직관적으로 판단할 수 있게 하였습니다.

<br/>

**관심 사이트 상세**

- 최대 10년 간의 홈페이지가 담긴 카드를 보여줍니다.
- 매년 1월 1일 기준으로 가장 가깝게 저장된 날짜의 홈페이지를 확인할 수 있습니다.
- 카드 좌측 상단에 해당 년도가 나타나며, 년도 우측에는 저장된 홈페이지의 정확한 날짜를 보여줍니다.
- 카드를 클릭하면 해당 년도의 홈페이지를 확인할 수 있는 사이트가 새 창으로 열립니다.
- 저장된 홈페이지가 없을 경우, 안내 문구와 홈으로 이동할 수 있는 버튼이 나타납니다.

<br/>

### 🔖 추가 기능

**사이트 별명 설정**

- 별명을 사용하는 것이 URL을 사용하는 것보다 사용자가 한 눈에 어떤 사이트인지 알아보기 쉬울 것이라고 판단했습니다.
- UI를 고려하여 최대 5자 까지의 별명을 설정할 수 있도록 했습니다.

```typescript
// /components/organisms/MainPage/SearchBar/index.tsx
...
<input
  placeholder="별명을 입력하세요. (최대 5자)"
  {...register("nickname", {
    required: MESSAGE_SEARCH_ERROR.NICKNAME_REQUIRED,
    maxLength: {
      value: 5,
      message: MESSAGE_SEARCH_ERROR.NICKNAME_LENGTH,
    },
  })}
/>
...
```

<details>
  <summary>코드</summary>
  <div markdown='1'>
    ```
    // /components/organisms/MainPage/SearchBar/index.tsx
      ...
      <input
        placeholder="별명을 입력하세요. (최대 5자)"
        {...register("nickname", {
          required: MESSAGE_SEARCH_ERROR.NICKNAME_REQUIRED,
          maxLength: {
            value: 5,
            message: MESSAGE_SEARCH_ERROR.NICKNAME_LENGTH,
          },
        })}
      />
    ```
  </div>
</details>





<br/>

**주소 파싱**

- 관심 사이트 카드의 URL은 최대 2줄까지 노출됩니다.
- 따라서 URL에서의 핵심적인 정보만 노출시키기 위해 URL의 프로토콜 이후부터 나타나도록 했습니다.

**주소 중복 검사**

```typescript
// /components/organisms/MainPage/SearchBar/index.tsx
...
const onValid = ({ nickname, url }: FieldValues) => {
  ...

  const data: IWishlistItem = {
    nickname,
    url: urlParsing(url),
  };

  ...
};
...

// /utils/urlParsing.ts
const urlParsing = (url: string) => {
  let parsed_url = [];

  if (url.startsWith("http")) {
    parsed_url = url.split("://");
    parsed_url[0] += "://";
  } else {
    parsed_url = ["", url];
  }

  if (url.endsWith("/")) {
    parsed_url[1] = parsed_url[1].slice(0, -1);
  }

  return parsed_url;
};
```

**URL 목록 캐싱**

- 

<br/>

### 🧑🏻‍💻 실행 방법

```bash
npm install
npm start
```

<br/>

### 🛠️ 기술 스택

- `TypeScript`, `React`

- `Recoil`, `React-Query`

    : 

- `React-hook-form`

    : 

- `Styled-component`

- `Netrify`

<br/>

### ✉️ 마치며

안녕하세요 먼저 귀한 시간 내시어 과제를 검토해주셔서 정말 감사드립니다!

과제를 수행하며 

