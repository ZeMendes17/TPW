import {Mammal} from "./Mammal";

export abstract class Canine extends Mammal {
    static nCanines :number = 0;
    race: string;

    constructor(race:string) {
        super();
        this.race = race;
    }
}