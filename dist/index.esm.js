import{resolveComponent as t,openBlock as e,createBlock as n,withCtx as o,createTextVNode as r,toDisplayString as d}from"vue";var a={__name:"RouterBtn",props:{path:{type:String,required:!0},buttonText:{type:String,required:!0}},setup:a=>(i,u)=>{const p=t("router-link");return e(),n(p,{to:a.path,class:"button"},{default:o((()=>[r(d(a.buttonText),1)])),_:1},8,["to"])}};!function(t,e){void 0===e&&(e={});var n=e.insertAt;if("undefined"!=typeof document){var o=document.head||document.getElementsByTagName("head")[0],r=document.createElement("style");r.type="text/css","top"===n&&o.firstChild?o.insertBefore(r,o.firstChild):o.appendChild(r),r.styleSheet?r.styleSheet.cssText=t:r.appendChild(document.createTextNode(t))}}("\n.button[data-v-4f30d4d3] {\n\tdisplay: inline-block;\n\tpadding: 10px 20px;\n\tcolor: white;\n\tbackground-color: #007bff;\n\tborder: none;\n\tborder-radius: 4px;\n\ttext-align: center;\n\ttext-decoration: none;\n\tfont-size: 16px;\n}\n.button[data-v-4f30d4d3]:hover {\n\tbackground-color: #0056b3;\n}\n\n"),a.__scopeId="data-v-4f30d4d3",a.__file="src/components/RouterBtn.vue";export{a as RouterBtn};
