<script>
    export let frontImgPath;
    export let backImgPath;
    export let isIdenticalBack;
    export let identifier;
</script>

<main>
    <div class="flip-card">
        <div class="flip-card-inner">
            <div class="flip-card-front">
                <img src="{frontImgPath}" alt="{identifier} front" />
            </div>
            <div class="flip-card-back">
                {#if isIdenticalBack}
                    <img src="{frontImgPath}" alt="{identifier} back (identical to front)" />
                {:else if backImgPath}
                    <img src="{backImgPath}" alt="{identifier} back" />
                {:else}
                    <p>Bu kart tek yüzlüdür.</p>
                {/if}
            </div>
        </div>
    </div>
</main>

<style>
    .flip-card {
        background-color: transparent;
        width: 320px;
        height: 180px;
        perspective: 1000px;
    }

    .flip-card-inner {
        position: relative;
        width: 100%;
        height: 100%;
        text-align: center;
        transition: transform 0.8s;
        transform-style: preserve-3d;
    }

    .flip-card:hover .flip-card-inner {
        transform: rotateY(180deg);
    }

    .flip-card-front, .flip-card-back {
        color: black;
        background-color: #fff;
        position: absolute;
        width: 100%;
        height: 100%;
        -webkit-backface-visibility: hidden;
        backface-visibility: hidden;
    }

    .flip-card-back {
        transform: rotateY(180deg);
    }
</style>
