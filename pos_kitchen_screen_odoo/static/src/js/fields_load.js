odoo.define('pos_kitchen_screen_odoo.models', function (require) {
    "use strict";
    var { PosGlobalState, Order} = require('point_of_sale.models');
    const Registries = require('point_of_sale.Registries');

    const PosSessionOrdersPosGlobalState = (PosGlobalState) => class PosSessionOrdersPosGlobalState extends PosGlobalState {
    //load the PosOrders and pos order lines
    async _processData(loadedData) {
        await super._processData(...arguments);
        this.pos_orders = loadedData['pos.order'];
        this.pos_order_lines = loadedData['pos.order.line'];
        }
        }
    Registries.Model.extend(PosGlobalState, PosSessionOrdersPosGlobalState);
});
