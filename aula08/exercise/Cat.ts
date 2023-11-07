import {Feline} from './Feline';

export class Cat extends Feline {
    static nCats :number = 0;
    name: string;
    meow: string = 'Meow! Meow!';

    constructor(family:string, name:string) {
        super(family);
        this.name = name;
        Cat.nCats++;
    }


    talk() {
        return super.talk() + ' ' + this.meow;
    }
}