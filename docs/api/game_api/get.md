# Game

A game is a set that can be accessed to build the puzzle match. It has a slot and a set of pieces with textures. You usually get it at the beginning.

GET /game
---

This endpoint gives you access to a list of all topics available in the game grouped by game.

**Auth required** : YES

**Permissions required** : `isAuthenticated`

**Arguments**

* `all`: List all or only published. **Optional**

**Example Request**

```bash
GET https://desafioplaneta.com/api/game/
```

**Example Response**

[response_get_game.json](responses/response_get_game.json)


GET /game/`<id>`
---

This endpoint gives you access to a specific game available from its ID.

**Auth required** : YES

**Permissions required** : `isAuthenticated`

**Arguments**

* `game_id` - The ID of the game. **Required**.

**Example Request**

```bash
GET https://desafioplaneta.com/api/game/<id>/?api_key={YOUR API KEY}
```

**Example Response**

[response_get_game-id.json](responses/response_get_game-id.json)
