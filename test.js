const fs = require("fs");
const config = require("./config.json")

config.exercises.practice = config.exercises.practice.map(x => ({...x, status: "wip"}))
config.exercises.concept = config.exercises.concept.map(x => ({...x, status: "wip"}))

fs.writeFile("./config.json", JSON.stringify(config), (err) => {
    if (err) console.log(err);
    console.log("Successfully Written to File.");
});

