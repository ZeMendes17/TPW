import {Cat} from "./Cat";
import {Dog} from "./Dog";

let cat = new Cat('Felidae', 'Tom');
let dog = new Dog('Labrador');

console.log(cat.talk());
console.log(dog.talk());
console.log(cat.show());
console.log(dog.show());
console.log(cat);
console.log(dog);
console.log(cat instanceof Cat);
console.log(cat instanceof Dog);
console.log(dog instanceof Dog);
console.log(dog instanceof Cat);

