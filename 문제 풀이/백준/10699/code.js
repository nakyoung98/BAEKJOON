const date = new Date();
const monthNum = date.getUTCMonth() + 1;
const today =
  date.getUTCFullYear() + "-" + (monthNum < 10 ? "0" + String(monthNum) : String(monthNum)) + "-" + date.getUTCDate();
console.log(today);
