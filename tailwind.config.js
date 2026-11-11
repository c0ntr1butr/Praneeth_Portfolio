/** @type {import('tailwindcss').Config} */
module.exports = {
  content: ["./*.html", "./script.js"],
  theme: {
    extend: {
      colors: {
        paper: { DEFAULT: "#efefeb", 2: "#e6e6e1", card: "#f7f7f4" },
        ink: { DEFAULT: "#000000", 90: "#191919", 80: "#313130", 60: "#626260", 50: "#7b7b78", 30: "#acaca8" },
        line: "#d9d9d4",
        blue: "#000ce1",
      },
      fontFamily: {
        sans: ["Geist", "ui-sans-serif", "system-ui", "sans-serif"],
        mono: ["'Geist Mono'", "ui-monospace", "monospace"],
        serif: ["'Instrument Serif'", "ui-serif", "Georgia", "serif"],
      },
      maxWidth: { page: "84rem" },
      borderRadius: { card: "15px" },
    },
  },
  plugins: [],
};
