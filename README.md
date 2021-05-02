# Introduction

Le café est l’une des boissons les plus consommées dans le monde. Cependant, il existe de nombreux cafés différents les uns des autres, comme le café noir, l’espresso, le cappuccino et des dizaines d’autres encore. Ces cafés sont d’abord différents par le grain de café utilisé mais également et principalement par la machine à café utilisée. En effet il existe plus d’une dizaine de types de machines à cafés différentes. Chaque machine à café possède une méthode d’élaboration propre, et donc un résultat différent.<br>

<img src="./image/les_cafetiere_perco.png" alt="Les Types de cafetières" width="489"> 

Nous nous intéressons alors à deux types de cafetière, la cafetière italienne et le percolateur à café. En effet, ces deux machines à café utilisent un phénomène bien répandu pour faire le café, **la théorie de la percolation**.<br>


# Le sujet

**Qu'est-ce que la percolation ?** Le mot vient du latin percolatio signifiant « filtration ». Utilisé dans un grand nombre de situations, il évoque les notions de propagation et d'agglutination dans des milieux. On rencontre la percolation le plus souvent dans le passage d'un liquide dans un milieu poreux. La percolation dépend de plusieurs facteurs tels que la porosité, la densité et la capacité du milieu à absorber l'eau. <br>

Par exemple, lorsqu'on parle de l'infiltration des eaux de pluie dans les nappes phréatiques, on suppose que l'eau s'écoule dans la roche, mais encore faut-il que cette roche soit suffisamment poreuse pour le permettre. La théorie de la percolation permet de déterminer la porosité suffisante pour le permettre.<br>

Il existe un seuil critique de percolation. Si la probabilité est inférieure à ce seuil, il n'y a jamais percolation et si elle est supérieure à ce seuil, il y a toujours percolation. Le **seuil critique théorique de percolation est de 0.592746**.<br>

Le modèle théorique de la percolation est utilisé dans beaucoup d'autres domaines : la simulation de la propagation des épidémies ou des feux de forêts par exemple.<br>

Ci-dessous est représenté un schéma de fonctionnement de la cafetière italienne. La cafetière italienne permet d’obtenir des cafés espresso. Elle se compose de trois parties distinctes: le réservoir d’eau (partie basse de la cafetière), le filtre (où l’on dépose la mouture de café) et pour finir la partie haute de la cafetière où s’écoulera le café. Il suffit donc de remplir le réservoir d’eau, le filtre de café moulu et de mettre la cafetière à chauffer. L’eau va commencer à bouillir, la pression augmente et pousse la vapeur d’eau dans l'entonnoir vers la mouture. La vapeur d'eau percole à travers le café moulu et finit dans le compartiment supérieur sous forme de café.<br>

<p align="center">
  <img width="320" height="512" src="./image/schema_percolation.jpg">
</p>


Le but de notre simulation est alors d’approcher le seuil critique de percolation avec le percolateur à café. Ici, le fluide est représenté par l'eau chaude et le milieu poreux par la mouture de café. On s’intéressera ainsi aux conséquences que peuvent porter les différents facteurs tels que la perméabilité et la densité de la mouture sur le rendement du café.


# Le modèle

On a créé aini un programme en Python permettant de modéliser à l'aide d'une fenêtre Tkinter le phénomène de percolation du café.<br>

Lien vers le programme complet : <a href=""> C'est ici ! </a>


# La simulation
# Analyse critique

Dans le cas de la cafetière à filtre, la dilution de l'eau dans le café prend plus de temps, et donc les arômes sont plus concentrés.<br>

Dans le cas d'un expresso par exemple, la percolation se fait très rapidement, ne laissant pas la concentration en arôme prendre de l'ampleur. Bien sûr, il est possible d'ajuster cette concentration en utilisant une quantité de mouture plus importante pour une quantité d'eau moindre.<br>

# Perspectives et conclusion

## Lien vers la page du blog : <a href="blog.md"> C'est ici ! </a>

## Présentaion de l'équipe

<table>
    <tr>
        <td>KIRITHARAN Pagish</td>
        <td>VAZ Christian</td>
        <td>AUDIN Matthias</td>
        <td>KECHEK Filip</td>
    </tr>
</table>


Nous sommes actuellement en 1ère année de licence à [Sorbonne Université](https://www.sorbonne-universite.fr/) en [MIPI](http://licence.premiereannee.sorbonne-universite.fr/fr/la-licence-1ere-annee/portail-mipi.html).

<a href = "https://www.sorbonne-universite.fr/">
 <img src="./image/logo_su.png" width="250">
</a>
