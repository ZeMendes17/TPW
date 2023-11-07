"use strict";
Object.defineProperty(exports, "__esModule", { value: true });
exports.Animal = void 0;
var Animal = exports.Animal = /** @class */ (function () {
    function Animal(habitat) {
        if (habitat === void 0) { habitat = 'Earth'; }
        this.habitat = habitat;
        Animal.nAnimals++;
    }
    Animal.prototype.show = function () {
        return "We are ".concat(Animal.nAnimals, " animals and my habitat is: ").concat(this.habitat);
    };
    Animal.nAnimals = 0;
    return Animal;
}());
