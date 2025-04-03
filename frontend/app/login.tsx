import { StyleSheet, Text, View, Image, TouchableOpacity } from "react-native";
import { FontAwesome } from "@expo/vector-icons";
import { Link, useRouter } from "expo-router";

export default function LoginScreen() {
  const router = useRouter();

  const handleSignUpClick = () => {
    router.navigate("/signup");
  };

  return (
    <View style={styles.container}>
      <Image
        source={require("../assets/images/logo.png")}
        style={styles.image}
      />

      <Text style={styles.text}>Login with your social media accounts</Text>

      {/* Google */}
      <TouchableOpacity style={[styles.button, styles.buttonBorder]}>
        <FontAwesome name="google" size={24} color="#DB4437" />
        <Text style={[styles.buttonText, { color: "#0000008A" }]}>
          Continue with Google
        </Text>
      </TouchableOpacity>

      {/* Twitter */}
      <TouchableOpacity style={[styles.button, styles.buttonBorder]}>
        <FontAwesome name="twitter" size={24} color="#1D9BF0" />
        <Text style={[styles.buttonText, { color: "#1D9BF0" }]}>
          Continue with Twitter
        </Text>
      </TouchableOpacity>

      {/* GitHub */}
      <TouchableOpacity style={[styles.button, styles.buttonBorder]}>
        <FontAwesome name="github" size={24} color="##24292F" />
        <Text style={[styles.buttonText, { color: "#24292F" }]}>
          Continue with Github
        </Text>
      </TouchableOpacity>

      <TouchableOpacity
        style={[styles.button, styles.buttonBorder]}
        onPress={handleSignUpClick}
      >
        <FontAwesome name="user-plus" size={24} color="#000" />
        <Text style={[styles.buttonText, { color: "#24292F" }]}>Sign Up</Text>
      </TouchableOpacity>
    </View>
  );
}

const styles = StyleSheet.create({
  container: {
    flex: 1,
    justifyContent: "center",
    alignItems: "center",
    backgroundColor: "#fff",
  },
  text: {
    fontSize: 18,
    fontWeight: "bold",
    marginBottom: 20,
  },
  image: {
    width: "50%",
    height: "20%",
    marginBottom: 40,
    resizeMode: "contain",
  },
  button: {
    flexDirection: "row",
    alignItems: "center",
    width: "80%",
    paddingVertical: 15,
    paddingHorizontal: 20,
    borderRadius: 10,
    marginVertical: 10,
    justifyContent: "center",
    backgroundColor: "transparent",
    borderWidth: 1.5,
  },
  buttonBorder: {
    borderColor: "#000",
  },
  buttonText: {
    fontSize: 18,
    fontWeight: "bold",
    marginLeft: 10,
  },
});
