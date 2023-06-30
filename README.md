<<<<<<< HEAD

<html>
  <body>
    
<details>
  <summary>Toggle code</summary>

  ```tsx
  // /components/organisms/MainPage/SearchBar/index.tsx
  ...
  <input
    placeholder="Please enter a nickname (up to 5 characters)"
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

=======
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

<details>
  <summary>코드</summary>
  <div markdown='1'>
    ``` typescript
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
>>>>>>> 31899a56bc736fcc22fe00b10c304496028cb77f
</details>

  </body>
</html>
