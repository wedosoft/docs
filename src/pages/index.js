"use strict";
Object.defineProperty(exports, "__esModule", { value: true });
exports.default = HomeRedirect;
var react_1 = require("react");
var router_1 = require("@docusaurus/router");
function HomeRedirect() {
    var history = (0, router_1.useHistory)();
    (0, react_1.useEffect)(function () {
        history.replace('/intro');
    }, [history]);
    return null;
}
