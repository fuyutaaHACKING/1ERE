<html>
	<head>
		<style type="text/css">
			h1{								<!-- Le code suivant s'applique à tous les titres H1 -->
				text-align: center;
				background-color: #444444;
			}
			.p_important{					<!-- Le code suivant s'applique à toutes les balises ayant la classe p_important -->
				font-style : italic;
				font-family : cursive;
				background-color: #AAAAAA;
			}
		</style>
	</head>
	<body>
		<h1>Amazing <?php echo $_POST['pseudo']; ?></h1>	<!-- code PHP qui récupère la valeur du paramètre pseudo passé par la méthode POST -->
		<p class=p_important>Welcome !!!</p>
		<button id=btn_ret_home>Home</button>				<!-- bontons gérés -->
		<button id=btn_principal>Page principale</button>	<!--	par JavaScipt -->
	</body>
	<script type="text/javascript">
		let togg1 = document.getElementById("btn_ret_home");							<!-- Affecte une variable avec la référence du bouton "Home" grace à son id -->
		togg1.addEventListener("click", () => {window.location.href='/un_exemple/'})	<!-- excute le code ()=>... lors d'un clique sur le bouton "Home" -->
		
		let togg2 = document.getElementById("btn_principal");							<!-- Affecte une variable avec la référence du bouton "Page principale" grace à son id -->
		togg2.addEventListener("click", () => {											<!-- excute le code ()=>... lors d'un clique sur le bouton "Page principale" -->
			var addr = '/un_exemple/le_site.php?pseudo=';								<!-- Crée une URL -->
			var para = <?php echo json_encode($_POST['pseudo']); ?>;					<!-- 	avec le paramètre -->
			window.location.href=addr.concat(para)})									<!-- 		pseudo -->
	</script>
</html>