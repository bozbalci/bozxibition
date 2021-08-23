<script>
    import imageIndex from './imageIndex.json'
    import Card from "./components/Card.svelte";

    // const PICTURE_LIBRARY = "pictures/flat-thumbnails";
    const PICTURE_LIBRARY = "http://pandora.whatbox.ca:59931/~boz/masaj-pictures/flat-thumbnails";
    const cards = [];

    for (let collectionId in imageIndex) {
        for (let itemId in imageIndex[collectionId]) {
            const item = imageIndex[collectionId][itemId]

            cards.push(
                {
                    identifier: `${collectionId}/${itemId}`,
                    frontImgPath: `${PICTURE_LIBRARY}/${item.p[0]}`,
                    backImgPath: item.p[1] !== undefined ? `${PICTURE_LIBRARY}/${item.p[1]}` : null,
                    isIdenticalBack: item.m === "iback",
                }
            )
        }
    }
</script>

<main>
    <div class="cards-gallery">
        {#each cards as {identifier, frontImgPath, backImgPath, isIdenticalBack}}
            <Card identifier={identifier}
                  frontImgPath={frontImgPath}
                  backImgPath={backImgPath}
                  isIdenticalBack={isIdenticalBack}
            />
        {/each}
    </div>
</main>

<style>
    .cards-gallery {
        display: flex;
        flex-wrap: wrap;
        width: 100%;
    }
</style>
