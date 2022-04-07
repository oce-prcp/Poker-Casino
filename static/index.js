const play          = () => location.href = "/initialization";
const restart       = () => location.href = "/board";
const goHomePage    = () => location.href = "/";

const clickOnCardForReverse = thisCard => {
    let selectedCard = thisCard.getAttribute("data-card");
    let stateImg     = thisCard.getAttribute("src");

    stateImg === "/static/cards/back.png"
        ? stateImg = `/static/cards/${selectedCard}.png`
        : stateImg = `/static/cards/back.png`;

    thisCard.setAttribute("src", stateImg);
}
