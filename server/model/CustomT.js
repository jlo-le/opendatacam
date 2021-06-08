

// Recording has methods to persist data to DB as it grows
// The idea is never having all the data in memory as 
// trackerHistory can be quite huge

class CustomT {
    constructor(
        firstDate,
        lastDate,
        x,y,
        w,h,
        color,
        speed,
        direction
        ) {
        this.firstDate = firstDate
        this.lastDate = lastDate
        this.color = color
        this.x = x
        this.y = y
        this.w = w
        this.h = h
        this.speed = speed
        this.direction = direction
    }
}

module.exports = CustomT
