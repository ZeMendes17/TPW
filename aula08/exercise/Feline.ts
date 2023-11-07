import {Mammal} from "./Mammal";

export abstract class Feline extends Mammal {
    static nFelines :number = 0;
    family: string;

    constructor(family:string) {
        super();
        this.family = family;
    }
}