const getDateInText = () => {
  const year = new Date().getFullYear();
  const month = new Date().toLocaleString("default", { month: "short" });
  const day = new Date().getDate();
  return `${month} ${day}, ${year}`;
};
