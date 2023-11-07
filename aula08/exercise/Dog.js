"use strict";
var __extends = (this && this.__extends) || (function () {
    var extendStatics = function (d, b) {
        extendStatics = Object.setPrototypeOf ||
            ({ __proto__: [] } instanceof Array && function (d, b) { d.__proto__ = b; }) ||
            function (d, b) { for (var p in b) if (Object.prototype.hasOwnProperty.call(b, p)) d[p] = b[p]; };
        return extendStatics(d, b);
    };
    return function (d, b) {
        if (typeof b !== "function" && b !== null)
            throw new TypeError("Class extends value " + String(b) + " is not a constructor or null");
        extendStatics(d, b);
        function __() { this.constructor = d; }
        d.prototype = b === null ? Object.create(b) : (__.prototype = b.prototype, new __());
    };
})();
Object.defineProperty(exports, "__esModule", { value: true });
exports.Dog = void 0;
var Canine_1 = require("./Canine");
var Dog = exports.Dog = /** @class */ (function (_super) {
    __extends(Dog, _super);
    function Dog(race) {
        var _this = _super.call(this, race) || this;
        _this.bark = 'Woof! Woof!';
        return _this;
    }
    Dog.prototype.talk = function () {
        return _super.prototype.talk.call(this) + ' ' + this.bark;
    };
    Dog.nDogs = 0;
    return Dog;
}(Canine_1.Canine));
