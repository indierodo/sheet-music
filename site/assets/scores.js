"use strict"

function titleCase(str) {
    return str.split(' ').map(function(word) {
        if (word[0] == '(')
            return word.replace(word[1], word[1].toUpperCase());
        return word.replace(word[0], word[0].toUpperCase());
    }).join(' ');
}

function formatName(mscz) {
    let name = mscz.replace('./scores/', '').replace('.mscz', '').replaceAll('_', ' ')
    return titleCase(name)
}

function addScore(score) {
    let mscz = score["in"];
    let pdf = score["out"];
    let name = formatName(mscz)
    let liHtml = `<li class="collection-item"><a href="${pdf}"><span class="new badge red darken-4" data-badge-caption="">PDF</span></a><a href="${mscz}"><span class="new badge indigo darken-4" data-badge-caption="">MSCZ</span></a>${name}</li>`;
    let ul = document.getElementById('score-list');
    ul.innerHTML += liHtml;
}

function getScores() {
    fetch('./assets/scores.json')
        .then(response => {
            if (!response.ok) {
                throw new Error('Network response was not ok');
            }
            return response.json();
        })
        .then(scores => {
            scores.forEach(score => {
                addScore(score)
            });
        })
        .catch(error => {
            console.error('There was a problem with the fetch operation:', error);
        });
}

document.addEventListener('DOMContentLoaded', getScores);