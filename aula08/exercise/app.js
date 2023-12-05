"use strict";
Object.defineProperty(exports, "__esModule", { value: true });
var Cat_1 = require("./Cat");
var Dog_1 = require("./Dog");
var cat = new Cat_1.Cat('Felidae', 'Tom');
var dog = new Dog_1.Dog('Labrador');
console.log(cat.talk());
console.log(dog.talk());
console.log(cat.show());
console.log(dog.show());
console.log(cat);
console.log(dog);
console.log(cat instanceof Cat_1.Cat);
console.log(cat instanceof Dog_1.Dog);
console.log(dog instanceof Dog_1.Dog);
console.log(dog instanceof Cat_1.Cat);