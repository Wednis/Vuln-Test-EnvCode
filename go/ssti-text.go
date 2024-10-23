package main

import (
	"fmt"
	"html/template"
	"os"
	"os/exec"
)

type Config struct {
	SecretKey string
}

func (c Config) Evil(test string) string {
	out, _ := exec.Command(test).CombinedOutput()
	return string(out)
}

func main() {
	payload := "{{.Evil \"calc\"}}"
	payload = "{{.SecretKey}}"
	tmpl, err := template.New("").Parse(payload)
	if err != nil {
		fmt.Println(err)
	}
	c := Config{"123456"}
	tmpl.Execute(os.Stdout, c)
	// fmt.Println(d)
}
