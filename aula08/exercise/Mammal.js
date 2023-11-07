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
exports.Mammal = void 0;
var Animal_1 = require("./Animal");
var Mammal = exports.Mammal = /** @class */ (function (_super) {
    __extends(Mammal, _super);
    function Mammal() {
        var _this = _super.call(this) || this;
        Mammal.nMammals++;
        return _this;
    }
    Mammal.prototype.show = function () {
        return _super.prototype.show.call(this) + " and ".concat(Mammal.nMammals, " mammals");
    };
    Mammal.prototype.talk = function () {
        return 'Mammal is talking:';
    };
    Mammal.nMammals = 0;
    return Mammal;
}(Animal_1.Animal));
