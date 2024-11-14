import vue from "rollup-plugin-vue";
import resolve from "@rollup/plugin-node-resolve";
import commonjs from "@rollup/plugin-commonjs";
import postcss from "rollup-plugin-postcss";
import { terser } from "rollup-plugin-terser";

export default {
  input: "src/index.js",
  output: [
    {
      format: "es",
      file: "dist/index.esm.js",
    },
    {
      format: "cjs",
      file: "dist/index.cjs.js",
      exports: "named",
    },
  ],
  plugins: [
    vue(),
    postcss(),
    resolve(),
    commonjs(),
    terser(),
  ],
  external: ["vue"],
};
