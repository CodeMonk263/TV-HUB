module.exports = {
    module: {
      rules: [
        {
          test: /\.js$/,
          exclude: /node_modules/,
          use: {
            loader: "babel-loader",
            options: {
                presets: [
                    '@babel/preset-env',
                    '@babel/preset-react'
                ],
                plugins: [
                    '@babel/transform-runtime'
                ]
            }
          }
        },
        {
          test: /\.css$/,
          exclude: /node_modules/,
          loaders: ['style-loader', 'css-loader'],
         },
      ]
    }
  };