package com.example.smartlightcontrol

import android.os.Bundle
import androidx.activity.ComponentActivity
import androidx.activity.compose.setContent
import androidx.compose.foundation.layout.*
import androidx.compose.material3.*
import androidx.compose.runtime.*
import androidx.compose.ui.Alignment
import androidx.compose.ui.Modifier
import androidx.compose.ui.unit.dp
import androidx.compose.ui.unit.sp

class MainActivity : ComponentActivity() {

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)

        setContent {
            SmartLightScreen()
        }
    }
}

@Composable
fun SmartLightScreen() {

    var lightOn by remember {
        mutableStateOf(false)
    }

    Column(
        modifier = Modifier
            .fillMaxSize()
            .padding(20.dp),

        verticalArrangement = Arrangement.Center,
        horizontalAlignment = Alignment.CenterHorizontally

    ) {

        Text(
            text = "SMART LIGHT CONTROL",
            fontSize = 28.sp
        )

        Spacer(modifier = Modifier.height(30.dp))

        Text(
            text = if (lightOn)
                "💡 Light Status : ON"
            else
                "💡 Light Status : OFF",

            fontSize = 22.sp
        )

        Spacer(modifier = Modifier.height(30.dp))

        Button(
            onClick = { lightOn = true }
        ) {
            Text("Turn ON")
        }

        Spacer(modifier = Modifier.height(15.dp))

        Button(
            onClick = { lightOn = false }
        ) {
            Text("Turn OFF")
        }

        Spacer(modifier = Modifier.height(30.dp))

        Text(
            text = "Wi-Fi : Connected",
            fontSize = 18.sp
        )
    }
}