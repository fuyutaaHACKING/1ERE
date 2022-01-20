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
		<h1>Bienvenue à toi <?php echo $_GET['pseudo']; ?></h1> <!-- Code PHP qui recupère la valeur du paramètre pseudo "envoyé" par la méthode get-->
		<p>"Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum."</p>
		<p class=p_important>Inscrit toi => <a href=javascript:void(0); onclick=vers_la_page()>ici</a></p><!--création d'un lien hypertext géré par du code JavaScript -->
		<button id=btn_ret_home>Home</button><!-- bouton géré par JavaScript -->
	</body>
	<script type="text/javascript">
		let togg1 = document.getElementById("btn_ret_home");						<!--récupère une référence du bouton par son id -->
		togg1.addEventListener("click", () => {window.location.href='/un_exemple/'})<!--exécute le code donné lorsque le bouton est cliqué -->
		
		function vers_la_page(){													<!--fonction appelée lors d'un clique sur le lien hypertext -->
			const queryString = window.location.search;
			const urlParams = new URLSearchParams(queryString);
			window.location.href='inscription.html?pseudo='+urlParams.get('pseudo')
		}
	</script>
</html>