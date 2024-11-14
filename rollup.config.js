import vue from "rollup-plugin-vue";
import resolve from "@rollup/plugin-node-resolve";
import commonjs from "@rollup/plugin-commonjs";

export default {
  input: "src/index.js",
  output: {
    format: "es",
    file: "dist/index.js",
  },
  plugins: [vue(), resolve(), commonjs()],
  external: ["vue"],
};
