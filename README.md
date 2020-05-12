## OpenCV: Open Source Computer Vision Library


Modified to build a small opencv.js bundle. 

easy way to build (needs docker):
```
 docker run --rm --workdir /code -v "$(get-location):/code" "trzeci/emscripten:latest" python ./platforms/js/build_js.py build_wasm --build_wasm
```

for more info visit: https://docs.opencv.org/master/d4/da1/tutorial_js_setup.html 


### Resources

* Homepage: <https://opencv.org>
* Docs: <https://docs.opencv.org/master/>
* Q&A forum: <http://answers.opencv.org>
* Issue tracking: <https://github.com/opencv/opencv/issues>

### Contributing

Please read the [contribution guidelines](https://github.com/opencv/opencv/wiki/How_to_contribute) before starting work on a pull request.

#### Summary of the guidelines:

* One pull request per issue;
* Choose the right base branch;
* Include tests and documentation;
* Clean up "oops" commits before submitting;
* Follow the [coding style guide](https://github.com/opencv/opencv/wiki/Coding_Style_Guide).
