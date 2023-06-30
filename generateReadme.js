const fs = require('fs');

// Markdown content with the toggle and code block
const markdown = `
<details>
  <summary>Toggle code</summary>

  \`\`\`tsx
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
  \`\`\`

</details>
`;

// Generate the HTML output
const html = `
<html>
  <body>
    ${markdown}
  </body>
</html>
`;

// Write the generated HTML to README.md
fs.writeFileSync('README.md', html);