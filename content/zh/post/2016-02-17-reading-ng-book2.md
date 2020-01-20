+++
date = "2016-02-17T19:09:19+08:00"
title = "Reading ng-book 2"
slug = "reading-ng-book2"

+++

哈哈, 最近在同时学两个东西, 都是 `ngxxx` 一个是 `nginx`, 另一个就是 `angular`.

同样地, 这是一篇无聊的文章, 只是给我个人用来记录进度的.(不记录, 坚持不下来啊)

## 学习动机
* 目前工作一个项目用的 angular 1.x
* data 驱动 view
* 前端太 tmd 的乱, 框架一大堆, 看别人分析, 都希望出现一个统一的框架. 我希望是 angular.
* 想摆脱手写html, 手写js, 手写 css 的低端模式, 学个框架, 以后可以装逼说自己会前端了.

## 文档地址
* <https://www.ng-book.com/2/>
* 下载的pdf: `ng-book2-r32.pdf`

## 进度

### 2016-02-17

* 当前的 angular 2 状态是 beta.
* angular: <https://angular.io/>
* typescript: <http://www.typescriptlang.org/>
* 简单的看了下网上各路人马的评价, 在typescript跟es6中选择了typescript.
* TypeScript is a superset of JavaScript ES6 that adds types.
* ES5 == normal JavaScript
* ES6 == ES2015
* Angular 2 is written in TypeScript and generally that’s what everyone is using.
* Angular 2 itself is a javascript file.
* Shim. A shim is a library that brings a new API to an older environment, using only the means of that environment.
* Polyfill. A polyfill is a piece of code (or plugin) that provides the technology that you, the developer, expect the browser to provide natively. Flattening the API landscape if you will.

### 2016-05-18

#### Angular 2 项目基础
* package.json
* tsconfig.json
* tslint.json

#### Angular 2 依赖
* ES6 Shim
* Zones
* Reflect Metadata
* SystemJS

#### notes
* CSS 使用 Semantic-UI.
* reference(in .d.ts) 语句指定 typing 文件的路径.
* import 语句是来自 ES6, 叫做 destructuring.
* Component 是 Angular 1里的 directives 的新版本.
* 一个基础的 Component 包含两个部分: Component annotation 和 component definition class.
* 把 annotation 看做 metadata added to your code. (? 跟 python 的 docorator 类似吧)
* selector: angular自己的selector mix, 类似 CSS selector, XPath, JQuery selector.
* `npm run tsc` 编译.
* `npm run tsc:w` 编译并监听.
* `tsc --watch` 每次修改都编译.
* 读到 Page 16

### 2016-05-19
* `npm run go` 监听修改并serve, 注意 8080 端口不能被占用.
* array: Angular1 的 `ng-repeat` 在 Angular2 中类似的指令是 `NgFor`.
* `#newtitle` 语法叫做一个 `resolve`. 效果是让这个变量在这个 view 范围的的表达式有效.
* 绑定 input 到 value, newtitle 是一个 object, 代表这个 input DOM 元素, 类型是 HTMLInputElement. 可以访问 `newtitle.value`.
* 绑定 actions 到 events, 组件类的一个函数赋值给 (click) 属性.
* 反引号: ES6 语法, 反引号的字符串将会展开模板变量.
* 可以在 attribute values 里面使用模板.
* 在 Angular 1, directives 全局 match, 在 Angular 2, 你需要显式指定你用哪个组件(因此, 哪个 selector).
* 在 js 里, 默认传播 click 事件给所有的父组件.
* 一个好的实践是当写 Angular 代码时, 尽量将你使用的数据结构与组件代码隔离.
* 封装的原则: LoD, <https://en.wikipedia.org/wiki/Law_of_Demeter>
* train-wreck: 小心 long-method chaining `foo.bar.baz.bam`
* 读到 Page 42

### 2016-05-20
* MVC guideline: [Skinny Controller, Fat Model](http://weblog.jamisbuck.org/2006/10/18/skinny-controller-fat-model)
* 核心理念是: 将大多数我们的 domain logic 移动到我们的 models, 因此我们的 components 尽可能做最少的工作.
* 数组的两种表示: 1. 普通: Article[]; 2. generics: Array<Article>.
* Component 的 attribute: inputs
* 创建 coimponent 的核心不仅仅是封装, 而且是为了重用.

#### 总结编写 Angular 2 应用步骤
1. 将你的应用分解成 components.
2. 创建 view.
3. 定义你的 model.
4. 显示你的 model.
5. 添加互动.

#### typescript
* ES6 = ES5 + classes + modules
* TypeScript = ES6 + types + annotations
* transpiler / transcompiler : TypeScript -> ES5.
* TypeScript to ES5 有一个单一的 transpiler, 由核心 TypeScript team 开发.
* ES6 to ES5 有两个 transpiler: [traceur](https://github.com/google/traceur- compiler) (by google), [babel](https://babeljs.io/) (by js community).
* REPL: ts-node, tsun
* number: 在TS中, 所有的number都是浮点数.
* any: any 是默认类型, 如果我们忽略给一个变量指定类型,
* classes: 在 ES5 中, OO是通过 prototype-based objects 实现的.
* 最佳实践, 关于补充js中没有class: <https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide>
* oo in js: <https://developer.mozilla.org/en-US/docs/Web/JavaScript/Introduction_to_Object-Oriented_JavaScript>
* class 有 properties, methods, constructors.
* A void value is also a valid any value.
* constructor: 必须被命名为: constructor. 每个 class 只能有一个 constructor.
* inheritance in ES5: <https://developer.mozilla.org/en-US/docs/Web/JavaScript/Inheritance_and_the_prototype_chain>
* inheritance: 使用 extends 关键字.
* Utilities(语法糖): ES6 提供一些语法糖: 1. fat arrow function syntax; 2. template strings;
* Fat Arrow Function (=>): 是一个缩写来写函数.
* 在 ES5 中, 如果我们想要使用一个函数作为参数, 我们需要使用 function 关键字和 {}.
* => 语法的一个重要特性是, 他和包围他的代码使用相同的 this. 这与你在 JS 中创建一个普通函数不同.
* 通常当你在 JS 中写一个函数时, 这个函数被分配他自己的 this.
* => 函数是一个很好的方法来清理你的 inline 函数. 他使在JS中使用高阶函数更简单.
* Template Strings: 在 ES6 中, 新的 template strings 被引入. 两个好的特性: 1. Varaibles within strings. 2. Multi-line strings.
* Variables in strings: 也叫 string interpolation. 要使用反引号, 不能使用单引号或者双引号.
* Angualr 2应用由 Component 组成(a tree of components), 一种理解 Component 的方式是教会浏览器新 tag.
* Angular 2 的 Component 和 Angular 1 的 directive 类似. 同时, Angular 2 也有 directive.
* component 是 composable.
* Angular 2 没有指定一个 model library.
* 读到 Page 76.

##### TypeScript 比 ES5 多的特性
* types
* classes
* annotations
* imports
* language utilities (e.g. desctructuring)

### 2016-05-26
* componet decorator: 包含一个 selector, 一个 template.
* component controller: 由一个 class 定义.
* component selector: 两种写法.
```
<inventory-app></inventory-app>
```

```
<div inventory-app></div>
```
* 添加实例到组件里来显示子组件.
* template binding: `{{...}}`, 里面不仅仅是一个变量, 是一个表达式.
* Inputs 和 Outputs: `[squareBrackets]` 传入 inputs, `(parenthesis)` 处理 outputs.
* 数据流入你的组件, 通过 input binding, 事件流出你的组件, 通过 output binding.
* 可以把 input + output bindings 看做你的组件的 public API.
* component inputs:
* Observer pattern: <https://en.wikipedia.org/wiki/Observer_pattern>
