const express = require('express')
const history = require('connect-history-api-fallback')
const app = express()

app.use(history())
app.use(express.static('dist'))

app.listen(3000, () => {
  console.log('Server running on port 3000')
}) 