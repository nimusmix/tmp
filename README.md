
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

</details>

  </body>
</html>
