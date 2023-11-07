import { Animal } from './Animal';

export abstract class Mammal extends Animal {
    static nMammals :number = 0;

    constructor() {
        super();
        Mammal.nMammals++;
    }

    show() {
        return super.show() + ` and ${Mammal.nMammals} mammals`;
    }

    talk() {
        return 'Mammal is talking:'
    }
}