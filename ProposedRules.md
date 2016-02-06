## Proposed Rules

* comment: for comments.
  * line: line comments, we specialize further so that the type of comment start character(s) can be extracted from the scope.
    * double-slash: `//` comment
    * double-dash: `--` comment
    * number-sign: `#` comment
    * percentage: `%` comment
    * character: other types of line comments.
  * block: multi-line comments like `/* … */` and `<-- … -->`.
    * documentation: embedded documentation.
  * todo: comments are often used to take notes.
  So if it nice when the syntax highlight words such as TODO, XXX, HACK, ...

* constant: various forms of constants.
  * numeric: those which represent numbers, e.g. `42`, `1.3f`, `0x4AB1U`.
  * character: those which represent characters, e.g. `&lt;`, `\e`, `\031`.
    * escape: escape sequences like `\e` would be constant.character.escape.
  * language: constants (generally) provided by the language which are “special” like `true`, `false`, `nil`, `YES`, `NO`, etc.
  * other: other constants, e.g. colors in CSS.

* entity: an entity refers to a larger part of the document, for example a chapter, class, function, or tag.
The scope entity is used only for tagging a declaration. For example `entity.name.class` will only be used on `Foo` in the following code,
but the code between brackets will wear a `meta.class.body` scope. `class Foo { ... }`

  * name: we are naming the larger entity.
    * function: the name of a function.
    * type: the name of a type declaration or class.
    * class: redundant with type but most languages use `class` instead of `type`
    * tag: a tag name or any annotation (like `@obsolete` in java).
    * section: the name is the name of a section/heading.
  * other: other entities.
    * inherited-class: the superclass/baseclass name.
    * attribute-name: the name of an attribute (mainly in tags).

* invalid: stuff which is “invalid”.
  * illegal: illegal, e.g. an ampersand or lower-than character in HTML (which is not part of an entity/tag).
  * deprecated: for deprecated stuff e.g. using an API function which is deprecated or using styling with strict HTML.

* keyword: keywords (when these do not fall into the other groups).
  * control: mainly related to flow control like continue, while, return, etc.
    * conditionnal: any of `if`, `then`, `else`
    * trycatch: any of `try`, `catch`, `finally` and `throw` or other keyword for handling exceptions
    * loop: any of `for`, `foreach`, `while`, ...
    * flow: keywords changing the normal flow of execution: `return`, `break`, `goto`, ...
  * operator: operators can either be textual (e.g. `or`) or be characters.
    * arithmetic: `+`, `-`, `*`, ...
    * logical: `&`, `|`, `or`, `and`, ...
    * comparaison: `<`, `>`, `==`, `is`, ...
    * assignement: for variable assignement `=`, `:=`, `+=`, ...
  * declaration
    * new: a whole scope just for `new`
  * other: other keywords.

* markup: this is for markup languages and generally applies to larger subsets of the text.
  * underline: underlined text.
    * link: this is for links, as a convenience this is derived from `markup.underline`
    so that if there is no theme rule which specifically targets `markup.underline.link`
    then it will inherit the underline style.
  * bold: bold text (text which is strong and similar should preferably be derived from this name).
  * heading: a section header. Optionally provide the heading level as the next element, for example `markup.heading.2.html` for `<h2>…</h2>` in HTML.
  * italic: italic text (text which is emphasized and similar should preferably be derived from this name).
  * list: list items.
    * numbered: numbered list items.
    * unnumbered: unnumbered list items.
  * quote: quoted (sometimes block quoted) text.
  * raw: text which is verbatim, e.g. code listings. Normally spell checking is disabled for markup.raw.
  * other: other markup constructs.

* meta: the meta scope is generally used to markup larger parts of the document.
`meta` design whole range of code not just a particular keyword.
`meta.xx.identifier` are meant to be picked up by symbol list.
It's nicer when the symbol list doesn't just display the name of a function but also it's arguments.
`meta.xx.body` marks the content of the method/function.
These scopes are used to delimite the code scopes.
  * class: for classes/types
    * identifier
    * body
  * function: for functions/methods
    * identifier
    * body
  * block: anything else: code inside `for` loop, `if`/`then`, ...
    * conditionnal
    * trycatch
    * loop

* storage: things relating to “storage”.
  * type: the type of something, class, function, var, etc.
  In some languages (like C) the `type` of a variable, like `int` is used both to mark the object as a variable and to precise that it's an integer.
  In this case consider using, `variable.other.type` instead.
    * class
    * function
    * variable
  * modifier: a storage modifier like static, final, abstract, etc.
    * access: modifiers changing the visibility of a method like `public`, `private`, ...

* string: strings.
  * quoted: quoted strings.
    * single: single quoted strings: 'foo'.
    * double: double quoted strings: "foo".
    * triple: triple quoted strings: """Python""".
    * other: other types of quoting: $'shell', %s{...}.
  * unquoted: for things like here-docs and here-strings.
  * interpolated: strings which are “evaluated”: `date`, $(pwd).
  * regexp: regular expressions: /(\w+)/.
  * other: other types of strings (should rarely be used).

* support: things provided by a framework or library should be below support.
  * function: functions provided by the framework/library. For example NSLog in Objective-C is support.function.
  * class: when the framework/library provides classes.
  * type: types provided by the framework/library, this is probably only used for languages derived from C,
  which has typedef (and struct). Most other languages would introduce new types as classes.
  * other: the above should be exhaustive, but for everything else use support.other.
  * variable: duplicate of `variable.language` shouldn't be used
  * constant: duplicate of `constant.language` shouldn't be used

* variable: variables. Not all languages allow easy identification (and thus markup) of these.
  Any of the following can be appended with `type`. Indeed types can be parameters (think of generic functions), arguments, provided by the language, ...
  * parameter: when the variable represent the parameter of a function.
  Used inside the function declaration or when calling a function when explicitly naming the parameter.
  * language: reserved language variables like this, super, self, etc.
  * other: other variables, like $some_variables.

* punctuation: Punctuation is really important for the compiler, let's make it useful for the programmers too !
All punctuations scopes should be appended with `begin` or `end` to tell if they are marking the begin or the end of something.
  * definition
    * arguments: the parenthesis for function call
    * arguments.type: the punctuation marking type arguments during function call
    * parameters: the parenthesis for function definition.
    There is a different scope for function calls and function definitions because most of the time you want to highlight function definitions, as they are the backbone of the code, while function calls are too common to be all highlighted.
    * parameters.type
    * expression: some languages introduce parenthesis for delimiting specific expressions.
    Like in C: `if(x == 0)`.
    * function: For punctuation delimiting inline function/lambda definition
    * array: For punctuation marking array, list, tuple, ...
    * string: Specific scope for the quotes
    * other
  * section: for punctuation enclosing large part of code. Most of the time it's `{` and `}`.
    * module: (also namespace, package, ...)
    * class
    * function
    * conditional
    * loop
    * trycatch
    * switch
    * other
    * merge: a special scope for marking annotation inserted by a version control merge.
    In git it's `<<<<<<<` and `>>>>>>>`.
    Matching them avoid the syntax to break when reading files being merged.
  * separator: for all the `,` dandling around :-)
    * accessor: for the dot `.` in `foo.bar()`
    * argument: for separating the argument of a function
    * array-element: for separating the values of an array, list, tuple
    * key-value: in python the `:` in `dictionary = {'a' : 0, 'b': 1}`
    * key-value.parameter: used to assign a value to a parameter.
    In python the `=` in `foo(bar=0)`
    * merge: in git it's `=======`
    * module: for punctuation inside module import
    * parameter
    * parameter.type
  * terminator.statement: a whole scope just for `;`
