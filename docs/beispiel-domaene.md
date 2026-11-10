*English · [Deutsch](beispiel-domaene.de.md)*

# Running example: “workshop shop” (orders)

One shared, small example for all workshops (JS/TS, Node.js, GraphQL, React, AWS, Reactive, Architecture, Knockout). Each lesson shows one part; in the full-stack mix they add up to one continuous application.

## Domain (deliberately small)
- **Product** `Product { id: ProductId, name: string, priceCents: number, stock: number }`
- **Order** `Order { id: OrderId, customerId: CustomerId, items: OrderItem[], status: 'draft' | 'placed' | 'paid' | 'shipped' | 'cancelled', createdAt: string (ISO 8601) }`
- **Line item** `OrderItem { productId: ProductId, quantity: number (≥ 1), priceCents: number }`
- **Customer** `Customer { id: CustomerId, name: string, email: string }`
- Money always as whole cents (`priceCents`), never as a decimal number.
- IDs as branded types (`type OrderId = string & { readonly __brand: 'OrderId' }`).

## Rules (for validation, aggregate, tests)
- An order in status `draft` may change its line items; from `placed` on it may not.
- `placed` only with at least one line item and sufficient stock.
- Total = Σ quantity × priceCents.
- Status sequence: draft → placed → paid → shipped; `cancelled` only from draft or placed.

## Shared zod schema (frontend and backend use the same one)
```ts
import { z } from 'zod'
export const OrderItemInput = z.strictObject({
  productId: z.string().min(1),
  quantity: z.number().int().min(1),
})
export const PlaceOrderInput = z.strictObject({
  customerId: z.string().min(1),
  items: z.array(OrderItemInput).min(1),
})
export type PlaceOrderInput = z.infer<typeof PlaceOrderInput>
```

## Mapping per workshop
- **JS/TS:** values, functions, arrays (sum, filter), branded IDs, zod schema, Pure Function `placeOrder`.
- **Node.js (Express 5):** REST API `/products`, `/orders` (POST place, GET list), validation with the schema, errors, database, tests.
- **GraphQL (Apollo):** schema `Product`, `Order`, `Query.orders`, `Mutation.placeOrder`, DataLoader for products, pagination of the orders.
- **React:** product list, cart (state/reducer), checkout form with the same zod schema, order overview (React Router).
- **AWS:** Lambda handler for placeOrder, DynamoDB model for orders, event “OrderPlaced” via EventBridge/SQS, Step Function for payment → shipping.
- **Reactive:** product search and filter as a stream, live status of the order.
- **Architecture:** Order as aggregate (consistency boundary), events OrderPlaced/OrderPaid, projection “open orders”, ADR “Why Event Sourcing only for orders”.
- **Knockout:** cart ViewModel with observables/computed (total).
- **Python:** money in cents as `int`, line items and order as dataclasses with `StrEnum` status, IDs as `NewType`, JSON fields as `TypedDict` in camelCase, error hierarchy `OrderError`, HTTP API with Flask 3, analysis of the orders with pandas.
