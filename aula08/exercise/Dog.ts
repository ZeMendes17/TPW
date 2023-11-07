import {Canine} from './Canine';

export class Dog extends Canine {
    static nDogs :number = 0;
    bark: string = 'Woof! Woof!';

    constructor(race:string) {
        super(race);
    }

    talk(): string {
        return super.talk() + ' ' + this.bark;
    }
}