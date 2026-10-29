# Durchgehendes Beispiel: „Werkstatt-Shop“ (Bestellungen)

Ein gemeinsames, kleines Beispiel für alle Workshops (JS/TS, Node.js, GraphQL, React, AWS, Reactive, Architektur, Knockout). Jede Lektion zeigt einen Ausschnitt; im Fullstack-Mix ergibt sich daraus eine durchgehende Anwendung.

## Domäne (bewusst klein)
- **Produkt** `Product { id: ProductId, name: string, priceCents: number, stock: number }`
- **Bestellung** `Order { id: OrderId, customerId: CustomerId, items: OrderItem[], status: 'draft' | 'placed' | 'paid' | 'shipped' | 'cancelled', createdAt: string (ISO 8601) }`
- **Position** `OrderItem { productId: ProductId, quantity: number (≥ 1), priceCents: number }`
- **Kunde** `Customer { id: CustomerId, name: string, email: string }`
- Geld immer als ganze Cent (`priceCents`), nie als Kommazahl.
- IDs als Branded Types (`type OrderId = string & { readonly __brand: 'OrderId' }`).

## Regeln (für Validierung, Aggregat, Tests)
- Eine Bestellung im Status `draft` darf Positionen ändern; ab `placed` nicht mehr.
- `placed` nur mit mindestens einer Position und ausreichend Bestand.
- Gesamtsumme = Σ quantity × priceCents.
- Statusfolge: draft → placed → paid → shipped; `cancelled` nur aus draft oder placed.

## Gemeinsames zod-Schema (Frontend und Backend nutzen dasselbe)
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

## Zuordnung je Workshop
- **JS/TS:** Werte, Funktionen, Arrays (Summe, Filter), Branded IDs, zod-Schema, reine Funktion `placeOrder`.
- **Node.js (Express 5):** REST-API `/products`, `/orders` (POST place, GET list), Validierung mit dem Schema, Fehler, Datenbank, Tests.
- **GraphQL (Apollo):** Schema `Product`, `Order`, `Query.orders`, `Mutation.placeOrder`, DataLoader für Produkte, Pagination der Bestellungen.
- **React:** Produktliste, Warenkorb (State/Reducer), Checkout-Formular mit demselben zod-Schema, Bestellübersicht (React Router).
- **AWS:** Lambda-Handler für placeOrder, DynamoDB-Modell für Orders, Event „OrderPlaced“ über EventBridge/SQS, Step Function für Bezahlung → Versand.
- **Reactive:** Suche/Filter der Produkte als Stream, Live-Status der Bestellung.
- **Architektur:** Order als Aggregat (Konsistenzgrenze), Events OrderPlaced/OrderPaid, Projektion „offene Bestellungen“, ADR „Warum Event Sourcing nur für Orders“.
- **Knockout:** Warenkorb-ViewModel mit observables/computed (Gesamtsumme).
- **Python:** Geld in Cent als `int`, Positionen und Bestellung als Dataclasses mit `StrEnum`-Status, IDs als `NewType`, JSON-Felder als `TypedDict` in camelCase, Fehlerhierarchie `OrderError`, HTTP-API mit Flask 3, Auswertung der Bestellungen mit pandas.
