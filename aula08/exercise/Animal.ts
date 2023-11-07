export abstract class Animal {
    static nAnimals :number = 0;
    habitat :string;

    constructor(habitat :string = 'Earth') {
        this.habitat = habitat;
        Animal.nAnimals++;
    }

    show() {
        return `We are ${Animal.nAnimals} animals and my habitat is: ${this.habitat}`;
    }
}

